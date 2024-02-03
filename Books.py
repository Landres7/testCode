from Book import Book, Author
import pickle

def saveState(state, tag="W_"):
    with open(f'{tag}state.pkl', 'wb') as fp:
        pickle.dump(state, fp)

def getState(tag="W_"):
    with open(f'{tag}state.pkl', 'rb') as fp:
        return pickle.load(fp)

def getBooksSavedState():
    newBooks = Books()
    newBooks.authors = getState("authors_")
    newBooks.books = getState("books_")
    return newBooks


class Books:
    def __init__(self):
        self.books =[]
        self.authors = []

    def _saveState(self):
        saveState(self.authors, "authors_")
        saveState(self.books, "books_")


        


    def addAuthor(self, name, nationality, alive):
        newKey = str(len(self.authors)+1)
        if name in [a.name for a in self.authors]:
            print("Author already exists")
            return False
        
        self.authors.append(Author(newKey, name, alive, [], nationality))
        return True

    def addBook(self, title, nPages, volume, authorName):
        newKey = str(len(self.books)+1)
        if title in [b.title for b in self.books]:
            print("Book Title already exists")
            return False

        author = self.getAuthorByName(authorName)
        newBook = Book(newKey, title, author, nPages, volume)
        self.books.append(newBook)
        author.addWrittenBook(newBook)
        
        self._saveState()
        
        return True

    def getBooksByIds(self, bookIds=[]):
        currentBooks = {b.bookId:b for b in self.books}
        return list(filter(lambda x: (x.bookId in bookIds), self.books))
     
        
    def getAuthorByName(self, name):
        for a in self.authors:
            if a.name == name:
                return a
        return None

    def getAuthorById(self, authorId):
        for a in self.authors:
            if a.authorId == authorId:
                return a
        return None





if __name__ == "__main__":
    bs1 = getBooksSavedState()

