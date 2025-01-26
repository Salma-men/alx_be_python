# book_class.py
class Book:
    def __init__(self, title, author, year):
        # Initialize the book instance with title, author, and year
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Print a message when the object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # String representation for human-readable output
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official string representation, used for debugging and recreating the object
        return f"Book('{self.title}', '{self.author}', {self.year})"
