import pandas as pd
import json

def load_raw_books(filepath="data/raw_books.json"):
    """Load raw books from JSON into a DataFrame."""
    with open(filepath, "r", encoding="utf-8") as f:
        books = json.load(f)
    df = pd.DataFrame(books)
    print(f"Loaded {len(df)} books into DataFrame.")
    return df

def clean_price(df):
    """Remove currency symbol and convert price to float."""
    df["price"] = df["price"].str.replace(r"[^\d.]", "", regex=True)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    return df

def clean_availability(df):
    """Convert availability text to boolean."""
    df["availability"] = df["availability"].str.strip().str.lower()
    df["availability"] = df["availability"] == "in stock"
    return df

def clean_rating(df):
    """Make sure rating is an integer."""
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df["rating"] = df["rating"].fillna(0).astype(int)
    return df

def drop_nulls(df):
    """Drop rows with missing title or price."""
    before = len(df)
    df = df.dropna(subset=["title", "price"])
    after = len(df)
    print(f"Dropped {before - after} rows with nulls.")
    return df

def clean_books(df):
    """Run all cleaning steps in order."""
    print("Cleaning data...")
    df = clean_price(df)
    df = clean_availability(df)
    df = clean_rating(df)
    df = drop_nulls(df)
    print("Cleaning complete.")
    print(df.dtypes)
    print(df.head())
    return df