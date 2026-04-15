import sqlite3

conn = sqlite3.connect("db/books.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM books")
print("Total books:", cursor.fetchone())

cursor.execute("SELECT title, price, rating FROM books LIMIT 5")
for row in cursor.fetchall():
    print(row)

conn.close()