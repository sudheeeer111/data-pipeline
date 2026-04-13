import requests
import time

BASE_URL = "https://books.toscrape.com/catalogue/"

def get_page(url):
    """Fetch a single page and return the HTML text."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises an error if status is 4xx/5xx
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_all_page_urls(total_pages=50):
    """Generate all catalogue page URLs."""
    urls = []
    for page_num in range(1, total_pages + 1):
        if page_num == 1:
            urls.append("https://books.toscrape.com/catalogue/page-1.html")
        else:
            urls.append(f"{BASE_URL}page-{page_num}.html")
    return urls

def get_total_pages(html):
    """Read how many pages exist from the first page."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    pager = soup.find("li", class_="current")
    if pager:
        # text looks like "Page 1 of 50"
        total = pager.text.strip().split()[-1]
        return int(total)
    return 1