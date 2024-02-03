

class Author:
    def __init__(self, authorId="0000", name="john doe", alive=True, booksWritten=[], nationality="PT"):
        self.authorId = authorId
        self.name = name
        self.alive = alive
        self.booksWritten = booksWritten
        self.nationality = nationality

    def addWrittenBook(self, book):
        assert type(book) == Book
        if not (book in self.booksWritten):
            self.booksWritten.append(book)
            return True
        raise Exception("Book already registered")

    def getName(self):
        return self.name


    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.authorId == self.authorId

    def __str__(self):
        return f'--[{self.authorId}]name: {self.name}; nationality: {self.nationality}; number of books: {str(len(self.booksWritten))}'

        
    def __repr__(self):
        return str(self)


class Book:
    def __init__(self, bookId="0000", title="testTitle", author=None, nPages=1, volume="vol0"):
        self.bookId = bookId
        self.title = title
        self.author = author
        self.nPages = nPages
        self.volume = volume


    def updateAuthor(self, author):
        assert type(author) == Author
        self.author = author


    def __eq__(self, other):
        if type(other) != type(self):
            return False

        return self.bookId == other.bookId

    def __str__(self):
        return f'--[{self.bookId}]Title: {self.title}; author: {self.author.getName()}; pages: {self.nPages}--'


    def __repr__(self):
        return str(self)



if __name__ == "__main__":
    a0 = Author()
    #a1 = Author("0010", "Ana", False, [], "PT")
    b0 = Book()
    b0.updateAuthor(a0)
    a0.addWrittenBook(b0)
    b1 = Book("0001", "mah name eh jeff", a1, 22,"Vol 1")
    a1.addWrittenBook(b1)
