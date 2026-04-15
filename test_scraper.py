from pipeline.cleaner import load_raw_books, clean_books

df = load_raw_books()
df = clean_books(df)

print("\nSample cleaned data:")
print(df[["title", "price", "rating", "availability"]].head(10))

print("\nData types:")
print(df.dtypes)

print("\nPrice stats:")
print(df["price"].describe())