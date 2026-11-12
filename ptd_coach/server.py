"""Loopback-only HTTP adapter for a fictitious local demo."""

from http.cookies import SimpleCookie, CookieError
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import hmac
import json
from pathlib import Path
import secrets
import threading
import time
from urllib.parse import urlsplit

from .identities import USERS, public_user
from .service import CASES, DomainError, exact_fields, require


WEB = Path(__file__).resolve().parents[1] / "web"
ASSETS = {"/": ("index.html", "text/html"), "/app.js": ("app.js", "text/javascript"),
          "/historique-a2": ("index.html", "text/html"),
          "/style.css": ("style.css", "text/css"),
          "/coach": ("coach.html", "text/html"), "/coach.js": ("coach.js", "text/javascript"),
          "/coach.css": ("coach.css", "text/css"),
          "/bibliotheque": ("library.html", "text/html"), "/library.js": ("library.js", "text/javascript"),
          "/library.css": ("library.css", "text/css")}
PROJECT_ASSETS = {"/": ("ptd.html", "text/html"), "/coach": ("ptd.html", "text/html"),
                  "/ptd.js": ("ptd.js", "text/javascript"), "/ptd.css": ("ptd.css", "text/css")}
COOKIE = "ptd_demo"


class DemoServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, address, service, chat=None, project=None):
        if address[0] != "127.0.0.1":
            raise ValueError("The fictitious demo must bind to 127.0.0.1")
        self.service = service
        self.chat = chat
        self.project = project
        self.sessions = {}
        self.session_lock = threading.Lock()
        super().__init__(address, Handler)
        # Browser cookies ignore ports. Keep the integrated demo and comparison
        # sessions independent when the user opens several local instances.
        self.cookie_name = f"{COOKIE}_{self.server_port}" if project is not None else COOKIE

    def new_session(self, user_id, old_token):
        token, csrf = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
        with self.session_lock:
            self.sessions = {k: v for k, v in self.sessions.items() if v["expires"] > time.time()}
            self.sessions.pop(old_token, None)
            self.sessions[token] = {"user_id": user_id, "csrf": csrf, "expires": time.time() + 8 * 3600}
        return token, csrf


class Handler(BaseHTTPRequestHandler):
    server_version = "PTDLocalDemo"
    sys_version = ""

    def log_message(self, *args):
        # Do not log URLs, input fields, cookies, prompts or responses.
        pass

    def reply(self, status, value, content_type="application/json", cookie=None, download=False):
        body = value if isinstance(value, bytes) else json.dumps(value, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'")
        if cookie:
            self.send_header("Set-Cookie", cookie)
        if download:
            filename = download if isinstance(download, str) else "ptd-a2-prive.json"
            self.send_header("Content-Disposition", 'attachment; filename="' + filename + '"')
        self.end_headers()
        self.wfile.write(body)

    def cookie_token(self):
        try:
            cookie = SimpleCookie(self.headers.get("Cookie", ""))
            session = cookie.get(self.server.cookie_name)
            return session.value if session else None
        except CookieError:
            return None

    def session(self):
        with self.server.session_lock:
            session = self.server.sessions.get(self.cookie_token())
            require(session is not None and session["expires"] > time.time(),
                    401, "unauthorized", "Ouvrez une session de démonstration.")
            return dict(session)

    def body(self):
        require(self.headers.get("Content-Type", "").split(";")[0].strip() == "application/json",
                415, "content_type", "Le corps doit être un objet JSON.")
        require(not self.headers.get("Transfer-Encoding"))
        try:
            length = int(self.headers.get("Content-Length", "0"))
            require(0 < length <= 32000, 413, "body_size", "Requête trop volumineuse ou vide.")
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            require(type(payload) is dict)
            return payload
        except (UnicodeError, ValueError):
            raise DomainError(400, "invalid_json", "JSON invalide.") from None

    def do_GET(self):
        self.dispatch("GET")

    def do_POST(self):
        self.dispatch("POST")

    def do_DELETE(self):
        self.dispatch("DELETE")

    def project_request(self, method, path, actor):
        project = self.server.project
        require(project is not None, 404, "not_found", "Atelier de projet indisponible.")
        if path == "/api/project":
            if method == "GET":
                return self.reply(200, project.snapshot(actor))
            if method == "POST":
                return self.reply(201, project.create(actor, self.body(), self.headers.get("Idempotency-Key")))
        if method == "POST":
            if path == "/api/project/next-week":
                return self.reply(200, project.next_week(actor, self.body()))
            parts = path.split("/")
            if len(parts) == 6 and parts[:4] == ["", "api", "project", "items"]:
                actions = {"update": project.update, "delete": project.delete, "confirm": project.confirm,
                           "share": project.share, "revoke": project.revoke}
                if parts[5] in actions:
                    return self.reply(200, actions[parts[5]](actor, parts[4], self.body()))
        raise DomainError(404, "not_found", "Page introuvable.")

    def dispatch(self, method):
        try:
            port = self.server.server_address[1]
            hosts = {"127.0.0.1:" + str(port), "localhost:" + str(port)}
            require(self.headers.get("Host") in hosts, 403, "host_forbidden", "Hôte refusé.")
            parsed = urlsplit(self.path)
            require(not parsed.scheme and not parsed.netloc and not parsed.query)
            path = parsed.path
            if method == "GET" and self.server.project is not None and path in PROJECT_ASSETS:
                name, mime = PROJECT_ASSETS[path]
                return self.reply(200, (WEB / name).read_bytes(), mime)
            if method == "GET" and path in ASSETS:
                name, mime = ASSETS[path]
                return self.reply(200, (WEB / name).read_bytes(), mime)
            if method == "GET" and path == "/api/library":
                from .library import catalogue
                return self.reply(200, catalogue())
            if method == "GET" and path == "/api/health":
                return self.reply(200, {"status": "ok", "provider": "mock", "demo": True})
            if method == "GET" and path == "/api/demo-users":
                return self.reply(200, [public_user(uid) for uid in USERS])
            if method != "GET":
                require(self.headers.get("Origin") in {"http://" + host for host in hosts},
                        403, "origin_forbidden", "Origine refusée.")
            if method == "POST" and path == "/api/demo-session":
                payload = self.body()
                exact_fields(payload, {"user_id"})
                uid = payload["user_id"]
                require(type(uid) is str and uid in USERS)
                token, csrf = self.server.new_session(uid, self.cookie_token())
                return self.reply(200, {"user": public_user(uid), "csrf": csrf},
                                  cookie=self.server.cookie_name + "=" + token + "; HttpOnly; SameSite=Strict; Path=/; Max-Age=28800")
            session = self.session()
            actor = session["user_id"]
            csrf = self.headers.get("X-CSRF-Token")
            if method != "GET" or csrf is not None:
                require(csrf is not None and csrf.isascii() and hmac.compare_digest(csrf, session["csrf"]),
                        403, "csrf_forbidden", "Session à recharger avant cette action.")
            if method == "GET" and path == "/api/me":
                return self.reply(200, {"user": public_user(actor), "csrf": session["csrf"]})
            if method == "DELETE" and path == "/api/demo-session":
                with self.server.session_lock:
                    self.server.sessions.pop(self.cookie_token(), None)
                return self.reply(200, {"logged_out": True},
                                  cookie=self.server.cookie_name + "=; HttpOnly; SameSite=Strict; Path=/; Max-Age=0")
            service = self.server.service
            key = self.headers.get("Idempotency-Key")
            if path == "/api/project" or path.startswith("/api/project/"):
                return self.project_request(method, path, actor)
            if path.startswith("/api/coach/"):
                chat = self.server.chat
                require(chat is not None, 503, "chat_unavailable", "Le coach conversationnel n'est pas activé sur ce serveur.")
                chat.student(actor)
                if path == "/api/coach/config" and method == "GET":
                    return self.reply(200, chat.public_config())
                if path == "/api/coach/resources" and method == "GET":
                    return self.reply(200, chat.context.resources)
                if path == "/api/coach/conversations":
                    if method == "GET":
                        return self.reply(200, chat.listing(actor))
                    if method == "POST":
                        return self.reply(201, chat.create(actor, key, self.body()))
                parts = path.strip("/").split("/")
                if len(parts) in (4, 5) and parts[:3] == ["api", "coach", "conversations"]:
                    cid = parts[3]
                    if len(parts) == 4 and method == "GET":
                        return self.reply(200, chat.conversation(actor, cid))
                    if len(parts) == 5 and parts[4] == "messages" and method == "POST":
                        return self.reply(200, chat.send(actor, cid, key, self.body()))
                    if len(parts) == 5 and parts[4] == "export" and method == "GET":
                        return self.reply(200, chat.export(actor, cid), download="ptd-conversation-fictive.json")
                raise DomainError(404, "not_found", "Page introuvable.")
            if method == "GET" and path == "/api/cases":
                return self.reply(200, CASES)
            if path == "/api/cycles":
                if method == "GET":
                    return self.reply(200, service.cycles(actor))
                if method == "POST":
                    return self.reply(201, service.create(actor, key, self.body()))
            if path == "/api/shares" and method == "GET":
                return self.reply(200, service.shares(actor))
            parts = path.strip("/").split("/")
            if len(parts) >= 3 and parts[:2] == ["api", "cycles"]:
                cycle_id = parts[2]
                if len(parts) == 3 and method == "GET":
                    return self.reply(200, service.cycle(actor, cycle_id))
                if len(parts) == 4:
                    if parts[3] == "actions" and method == "POST":
                        return self.reply(200, service.act(actor, cycle_id, key, self.body()))
                    if parts[3] == "shares" and method == "POST":
                        return self.reply(201, service.share(actor, cycle_id, key, self.body()))
                    if parts[3] == "export" and method == "GET":
                        return self.reply(200, service.export(actor, cycle_id), download=True)
            if len(parts) == 3 and parts[:2] == ["api", "shares"] and method == "DELETE":
                return self.reply(200, service.revoke(actor, parts[2], key, self.body()))
            raise DomainError(404, "not_found", "Page introuvable.")
        except DomainError as error:
            self.reply(error.status, {"error": {"code": error.code, "message": error.message}})
        except (BrokenPipeError, ConnectionResetError):
            pass
        except Exception:
            self.reply(500, {"error": {"code": "internal_error", "message": "Erreur locale. Réessayez après avoir rechargé la page."}})
