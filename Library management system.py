class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def get_category(self):
        if self.price>=1000:
            return"Premium"
        elif self.price>=500:
            return"standard"
        else:
            return"basic"


    def display(self):
        print("Title:",self.title)
        print("Author of book:",self.author)
        print("Price of book",self.price)
        print("Category of Book:",self.get_category())
        print("-------------------------------------")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
    def display_books(self):
        print("\n Library books")
        for book in self.books:
            book.display()

library = Library()

book1 = Book("Python Programming", "John Smith", 1200)
book2 = Book("Data Structures", "Robert Brown", 750)
book3 = Book("C Programming", "Dennis Ritchie", 400)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()