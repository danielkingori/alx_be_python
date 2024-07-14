class Book:
    def __init__(self, title, author, is_checked_out=False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out

    def check_out(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False

    def is_available(self):
        return not self.is_checked_out

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
        print(f"Added book: {book.title}")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"Checked out {title}")
                else:
                    print(f"{title} has already been checked out.")
                return
        print(f"{title} is not available in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"Returned {title}")
                else:
                    print(f"{title} was not checked out.")
                return
        print(f"{title} is not a part of the library collection.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author}")
        else:
            print("No books are currently available.")