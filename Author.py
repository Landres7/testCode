from Book import Book

class Author:
    def __init__(self, authorId="0000", name="john doe", alive=True, booksWritten=[], nationality="PT"):
        self.authorId = authorId
        self.name = name
        self.alive = alive
        self.booksWritten = booksWritten
        self.nationality = nationality

    def addWrittenBook(self, book):
        assert type(book) == Book
        if not book in self.booksWritten:
            self.booksWritten.append(book)
            return True
        return False


    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.authorId == self.authorId

    def __str__(self):
        return f'--[{self.authorId}]name: {self.name}; nationality: {self.nationality}; number of books: {str(len(self.booksWritten))}'



