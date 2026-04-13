from bs4 import BeautifulSoup
from scraper.models import Book

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def parse_books(html, category="General"):
    """Parse all books from a single catalogue page."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    articles = soup.find_all("article", class_="product_pod")

    for article in articles:
        # Title
        title = article.h3.a["title"]

        # Price
        price = article.find("p", class_="price_color").text.strip()

        # Rating — stored as a CSS class like "star-rating Three"
        rating_word = article.find("p", class_="star-rating")["class"][1]
        rating = RATING_MAP.get(rating_word, 0)

        # Availability
        availability = article.find("p", class_="availability").text.strip()

        book = Book(
            title=title,
            price=price,
            rating=rating,
            category=category,
            availability=availability
        )
        books.append(book)

    return books