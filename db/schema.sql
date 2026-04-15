CREATE TABLE IF NOT EXISTS books (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    title        TEXT NOT NULL,
    price        REAL,
    rating       INTEGER,
    category     TEXT,
    availability TEXT
);