import pandas as pd
import numpy as np
from pipeline.cleaner import load_raw_books, clean_books

def run_report():
    # Load and clean data
    df = load_raw_books()
    df = clean_books(df)

    print("\n" + "="*50)
    print("        BOOK STORE ANALYSIS REPORT")
    print("="*50)

    # ── 1. Overall stats ──────────────────────────
    print("\n📊 OVERALL STATS")
    print(f"  Total books      : {len(df)}")
    print(f"  Average price    : £{df['price'].mean():.2f}")
    print(f"  Cheapest book    : £{df['price'].min():.2f}")
    print(f"  Most expensive   : £{df['price'].max():.2f}")
    print(f"  Books in stock   : {df['availability'].sum()}")

    # ── 2. Rating distribution ────────────────────
    print("\n⭐ RATING DISTRIBUTION")
    rating_counts = df["rating"].value_counts().sort_index()
    for star, count in rating_counts.items():
        bar = "█" * (count // 10)
        print(f"  {star} star : {count:>4} books  {bar}")

    # ── 3. Top 5 categories by average price ─────
    print("\n💰 TOP 5 MOST EXPENSIVE CATEGORIES (avg price)")
    top_categories = (
        df.groupby("category")["price"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )
    for category, avg_price in top_categories.items():
        print(f"  {category:<30} £{avg_price:.2f}")

    # ── 4. Top 10 rated books under £15 ──────────
    print("\n🏆 TOP 10 RATED BOOKS UNDER £15")
    cheap_top = (
        df[df["price"] < 15]
        .sort_values(["rating", "price"], ascending=[False, True])
        .head(10)
    )
    for _, row in cheap_top.iterrows():
        print(f"  {row['rating']}⭐  £{row['price']:.2f}  {row['title'][:45]}")

    # ── 5. NumPy stats on price ───────────────────
    print("\n📈 PRICE ANALYSIS (NumPy)")
    prices = np.array(df["price"])
    print(f"  Mean             : £{np.mean(prices):.2f}")
    print(f"  Median           : £{np.median(prices):.2f}")
    print(f"  Std deviation    : £{np.std(prices):.2f}")
    print(f"  75th percentile  : £{np.percentile(prices, 75):.2f}")
    print(f"  Books above avg  : {np.sum(prices > np.mean(prices))}")

    # ── 6. Category with most 5-star books ───────
    print("\n🌟 CATEGORIES WITH MOST 5-STAR BOOKS")
    five_star = (
        df[df["rating"] == 5]
        .groupby("category")
        .size()
        .sort_values(ascending=False)
        .head(5)
    )
    for category, count in five_star.items():
        print(f"  {category:<30} {count} books")

    print("\n" + "="*50)

if __name__ == "__main__":
    run_report()