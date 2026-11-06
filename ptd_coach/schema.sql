CREATE TABLE cycles (
    id TEXT PRIMARY KEY,
    owner_id TEXT NOT NULL,
    team_id TEXT NOT NULL,
    state TEXT NOT NULL,
    version INTEGER NOT NULL,
    case_id TEXT NOT NULL,
    scenario_version TEXT NOT NULL,
    competency_version TEXT NOT NULL,
    data TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE INDEX cycles_owner ON cycles(owner_id);
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    cycle_id TEXT NOT NULL REFERENCES cycles(id),
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE shares (
    id TEXT PRIMARY KEY,
    cycle_id TEXT NOT NULL REFERENCES cycles(id),
    owner_id TEXT NOT NULL,
    recipient_id TEXT NOT NULL,
    text TEXT NOT NULL,
    revoked INTEGER NOT NULL DEFAULT 0,
    version INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL
);
CREATE INDEX shares_recipient ON shares(recipient_id, revoked);
CREATE TABLE events (
    id INTEGER PRIMARY KEY,
    actor_id TEXT NOT NULL,
    kind TEXT NOT NULL,
    object_id TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE commands (
    actor_id TEXT NOT NULL,
    command_key TEXT NOT NULL,
    fingerprint TEXT NOT NULL,
    response TEXT NOT NULL,
    PRIMARY KEY (actor_id, command_key)
);
PRAGMA user_version = 1;
