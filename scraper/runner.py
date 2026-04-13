import json
import time
from scraper.fetcher import get_page, get_all_page_urls, get_total_pages
from scraper.parser import parse_books

def scrape_all_books():
    """Scrape all pages and return a list of book dicts."""
    
    # Step 1: get the first page to find total pages
    first_url = "https://books.toscrape.com/catalogue/page-1.html"
    print("Fetching first page...")
    first_html = get_page(first_url)
    total_pages = get_total_pages(first_html)
    print(f"Found {total_pages} pages to scrape.")

    all_books = []

    # Step 2: loop through every page
    urls = get_all_page_urls(total_pages)

    for i, url in enumerate(urls, start=1):
        print(f"Scraping page {i}/{total_pages}...", end="\r")
        
        html = get_page(url)
        if html:
            books = parse_books(html)
            all_books.extend([book.to_dict() for book in books])
        
        time.sleep(0.5)  # be polite, don't hammer the server

    print(f"\nDone! Scraped {len(all_books)} books.")
    return all_books


def save_to_json(books, filepath="data/raw_books.json"):
    """Save list of book dicts to a JSON file."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=2, ensure_ascii=False)
    print(f"Saved to {filepath}")