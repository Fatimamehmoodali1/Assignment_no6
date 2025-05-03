class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Increment count whenever a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_total(cls):
        print(f"Total books: {cls.total_books}")

# Example usage:
b1 = Book("Python Basics")
b2 = Book("Advanced Python")
Book.display_total()
