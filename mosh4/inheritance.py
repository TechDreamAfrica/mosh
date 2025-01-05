class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def __str__(self):
        return self.title

    @classmethod
    def initials(cls):
        return cls("","", 0, "")

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

class TextBook(Book):
    def co_author(self, co_author):
        return self.co_author

book1 = Book.initials()
print(book1)

book2 = Book("In the Chest of a Woman", "Efo Kojo Mawugbe", 20, "Literature")
print(book2.get_title())