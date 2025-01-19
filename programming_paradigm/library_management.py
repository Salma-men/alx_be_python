# library_management.py

class Book:
    """A class to represent a book in the library."""

    def __init__(self, title, author):
        """
        Initialize the book with a title, an author, 
        and a private attribute _is_checked_out to track availability.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Successfully checked out '{title}'.")
                    return
        print(f"Sorry, '{title}' is either not available or already checked out.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Successfully returned '{title}'.")
                    return
        print(f"Sorry, '{title}' was not checked out.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
