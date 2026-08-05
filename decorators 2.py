def details(func):
    def wrapper(self):
        print("Book Details")
        func(self)
        print("Thank You")
    return wrapper

class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author

    @details
    def show(self):
        print("Title:", self.title)
        print("Author:", self.author)

b1 = Book("Python Basics", "ABC")
b1.show()