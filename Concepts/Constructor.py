# Default constructor
class Book:
    def __init__(self):
        self.name = "Python"
        self.author = "Guido Van Rossum"
        self.price = 700

book = Book()
print(book.name)
print(book.author)
print(book.price)

# Parameterized constructor
class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price =price

book = Book("Python", "Guido Van Rossum", 700)
print(f"{book.name} - {book.author} - {book.price}")


