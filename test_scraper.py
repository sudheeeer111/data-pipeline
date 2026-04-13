from scraper.runner import scrape_all_books, save_to_json

books = scrape_all_books()
save_to_json(books)