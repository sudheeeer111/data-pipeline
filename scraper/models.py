class Book:
    def __init__(self, title, price, rating, category, availability):
        self.title = title
        self.price = price          # raw string e.g. "£12.99"
        self.rating = rating        # raw string e.g. "Three"
        self.category = category
        self.availability = availability

    def __repr__(self):
        return f"Book(title={self.title!r}, price={self.price!r}, rating={self.rating!r})"

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "rating": self.rating,
            "category": self.category,
            "availability": self.availability
        }