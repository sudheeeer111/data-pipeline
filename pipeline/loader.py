import sqlite3
import json
import os

DB_PATH = "db/books.db"
SCHEMA_PATH = "db/schema.sql"

def get_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # lets us access columns by name
    return conn

def init_db():
    """Create the database and tables if they don't exist."""
    conn = get_connection()
    with open(SCHEMA_PATH, "r") as f:
        schema = f.read()
    conn.executescript(schema)
    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH}")

def insert_books(books):
    """Insert a list of book dicts into the database."""
    conn = get_connection()
    cursor = conn.cursor()

    inserted = 0
    skipped = 0

    for book in books:
        try:
            cursor.execute("""
                INSERT INTO books (title, price, rating, category, availability)
                VALUES (?, ?, ?, ?, ?)
            """, (
                book["title"],
                book["price"],
                book["rating"],
                book["category"],
                book["availability"]
            ))
            inserted += 1
        except sqlite3.IntegrityError:
            skipped += 1

    conn.commit()
    conn.close()
    print(f"Inserted {inserted} books. Skipped {skipped} duplicates.")

def load_books_from_json(filepath="data/raw_books.json"):
    """Load raw books from JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)