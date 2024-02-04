from Book import Book, Author
import pickle

def saveState(state, tag="W_"):
    with open(f'{tag}state.pkl', 'wb') as fp:
        pickle.dump(state, fp)

def getState(tag="W_"):
    with open(f'{tag}state.pkl', 'rb') as fp:
        return pickle.load(fp)

def getBooksSavedState(tag=""):
    newBooks = Books(tag)
    newBooks.authors = getState(tag+"authors_")
    newBooks.books = getState(tag+"books_")
    return newBooks


class Books:
    def __init__(self, tag=""):
        self.books =[]
        self.authors = []
        self.tag = tag

    def _saveState(self):
        saveState(self.authors, self.tag+"authors_")
        saveState(self.books, self.tag+"books_")

    def clearBookList(self):
        cleanList = []
        for b in self.books:
            if b.author:
                cleanList += [b]
        self.books = cleanList
        self._saveState()
        

    def getDictAuthors(self):
        return {"authors": [{"authorId":a.authorId, "name":a.name, "alive":a.alive, "booksWritten":a.getDictBooksWrittenList()} for a in self.authors]}



    def getDictBooks(self):
        return {"books": [{"bookId":b.bookId, "title":b.title, "author":b.author.name, "volume":b.volume} for b in self.books]}


    def addAuthor(self, name, nationality, alive):
        newKey = str(len(self.authors)+1)
        if name in [a.name for a in self.authors]:
            print("Author already exists")
            return False
        
        self.authors.append(Author(newKey, name, alive, [], nationality))
        return True

    def addBook(self, title, nPages, volume, authorName):
        author = self.getAuthorByName(authorName)
        if not author:
            raise Exception(f"Author {authorName} does not exist")
        
        newKey = str(len(self.books)+1)
        if title.lower() in [b.title.lower() for b in self.books]:
            raise Exception("Book Title already exists")
        
        newBook = Book(newKey, title, author, nPages, volume)
        self.books.append(newBook)
        author.addWrittenBook(newBook)
        
        self._saveState()
        
        return True

    def getBooksByIds(self, bookIds=[]):
        return list(filter(lambda x: (x.bookId in bookIds), self.books))

    def searchBooksByTitle(self, title):
        return list(filter(lambda b: title.lower() in b["title"].lower(), self.getDictBooks()["books"]))
     
        
    def getAuthorByName(self, name):
        for a in self.authors:
            if a.name.lower() == name.lower():
                return a
        return None

    def getAuthorById(self, authorId):
        for a in self.authors:
            if a.authorId == authorId:
                return a
        return None





if __name__ == "__main__":
    bs1 = getBooksSavedState()

