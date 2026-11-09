CREATE TABLE conversations (
    id TEXT PRIMARY KEY,
    scope TEXT NOT NULL CHECK (scope IN ('individual', 'collective')),
    owner_id TEXT NOT NULL,
    team_id TEXT NOT NULL,
    creation_key TEXT NOT NULL,
    version INTEGER NOT NULL DEFAULT 1,
    pending INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL,
    UNIQUE(owner_id, creation_key)
);
CREATE INDEX conversations_owner ON conversations(scope, owner_id);
CREATE INDEX conversations_team ON conversations(scope, team_id);
CREATE TABLE chat_messages (
    id INTEGER PRIMARY KEY,
    conversation_id TEXT NOT NULL REFERENCES conversations(id),
    role TEXT NOT NULL CHECK (role IN ('user', 'assistant')),
    content TEXT NOT NULL,
    author_id TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE TABLE chat_requests (
    actor_id TEXT NOT NULL,
    command_key TEXT NOT NULL,
    conversation_id TEXT NOT NULL REFERENCES conversations(id),
    fingerprint TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('pending', 'succeeded', 'failed')),
    metadata TEXT NOT NULL,
    error TEXT,
    created_at TEXT NOT NULL,
    PRIMARY KEY(actor_id, command_key)
);
PRAGMA user_version = 1;
