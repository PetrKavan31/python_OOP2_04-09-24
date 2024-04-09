class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def showInfo(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Pages: {}".format(self.pages))

    def __str__(self):
        return f"Title: {self.title}Author: {self.author}Pages: {self.pages}"

    def __add__(self, other):
        self.other = other
        return self.other


book1 = Book("Python Crash Course", "Eric Matthes", 624)
book2 = Book("JavaScript: The Goog Parts", "Douglas Crockford", 170)
book3 = Book("JavaScript: The Goog Parts", "Douglas Crockford", 1000)

# print(book1+book2)
print(book1)
book1.showInfo()

soucet = book1.pages + book2.pages + book3.pages
print(soucet)

