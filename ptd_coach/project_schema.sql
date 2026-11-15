CREATE TABLE IF NOT EXISTS semester_projects (
    team_id TEXT PRIMARY KEY,
    current_week INTEGER NOT NULL DEFAULT 1 CHECK (current_week BETWEEN 1 AND 52),
    version INTEGER NOT NULL DEFAULT 1 CHECK (version > 0)
);

CREATE TABLE IF NOT EXISTS project_items (
    id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL REFERENCES semester_projects(team_id),
    owner_id TEXT NOT NULL,
    scope TEXT NOT NULL CHECK (scope IN ('individual', 'collective')),
    kind TEXT NOT NULL CHECK (kind IN (
        'fact', 'hypothesis', 'proposal', 'requirement', 'criterion',
        'question', 'decision', 'obstacle', 'action', 'review', 'note'
    )),
    text TEXT NOT NULL,
    source TEXT NOT NULL,
    origin TEXT NOT NULL CHECK (origin IN ('human', 'ai')),
    week INTEGER NOT NULL CHECK (week BETWEEN 1 AND 52),
    confirmed_at TEXT,
    confirmed_by TEXT,
    confirmed_week INTEGER CHECK (confirmed_week BETWEEN 1 AND 52),
    shared_to TEXT,
    version INTEGER NOT NULL DEFAULT 1 CHECK (version > 0),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    CHECK ((confirmed_at IS NULL) = (confirmed_by IS NULL)),
    CHECK (shared_to IS NULL OR (scope = 'collective' AND confirmed_at IS NOT NULL))
);

CREATE INDEX IF NOT EXISTS project_items_team ON project_items(team_id, scope, owner_id);
CREATE INDEX IF NOT EXISTS project_items_share ON project_items(team_id, shared_to);

CREATE TABLE IF NOT EXISTS project_create_commands (
    actor_id TEXT NOT NULL,
    command_key TEXT NOT NULL,
    item_id TEXT UNIQUE REFERENCES project_items(id),
    fingerprint TEXT,
    PRIMARY KEY(actor_id, command_key),
    CHECK ((item_id IS NULL) = (fingerprint IS NULL))
);

CREATE TABLE IF NOT EXISTS project_share_audit (
    id INTEGER PRIMARY KEY,
    item_id TEXT NOT NULL,
    item_version INTEGER NOT NULL,
    actor_id TEXT NOT NULL,
    recipient_id TEXT NOT NULL,
    action TEXT NOT NULL CHECK (action IN ('share', 'revoke', 'revoke_on_edit', 'revoke_on_delete')),
    occurred_at TEXT NOT NULL
);
