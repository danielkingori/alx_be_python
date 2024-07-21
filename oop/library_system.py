class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} by {self.author}"
book1 = Book("things fall apart", "chinua")
book2 = Book("things sit bach apart", "linus")
book3 = Book("mool fall apart", "ton")
print(book1)
print(book2)
print(book3)

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    def borrow_books(self, book):
        self.borrowed_books.append(book)
    def __str__(self):
        return f"member: {self.name} borrowed books: {[str(book) for book in self.borrowed_books]}"
member1 = Member("simon")
member2 = Member("Kot")

member1.borrow_books(book1)
member2.borrow_books(book2)

print(member1,member2)