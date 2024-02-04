from Books import Books, getBooksSavedState
from Costumers import Costumers
##import os
##import pickle
##
##def saveState(state, tag="W_"):
##    with open(f'{tag}state.pkl', 'wb') as fp:
##        pickle.dump(state, fp)
##
##def getState(tag="W_"):
##    with open(f'{tag}state.pkl', 'rb') as fp:
##        return pickle.load(fp)


class BookStore:

    def __init__(self, tag="test_", getState=False, setState=False):
        self.tag = tag
        if getState:
            self.costumers = Costumers.getCustomersState(self.tag)
            self.books = getBooksSavedState(self.tag)
        else:
            self.costumers = Costumers(self.tag)
            self.books = Books(self.tag)

    def saveState(self):
        self.costumers.saveState()
        self.books._saveState()


    def registerCostumer(self, name, dob):
        return self.costumers.addCostumer(name, dob)
    

    def registerPurchaseByName(self, name, itemsPurchased, price, payed):
        return self.costumers.addPurchaseByName(name, itemsPurchased, price, payed)
        
    def registerPurchaseByTitle(self, name, title, price, payed):
        pass
        

    def registerAuthor(self, name, nationality, alive):
        return self.books.addAuthor(name, nationality, alive)


    def registerBook(self, title, nPages, volume, authorName):
        return self.books.addBook(title, nPages, volume, authorName)

    def getCostumers(self):
        return self.costumers.getCostumersDict()
        

    def getCostumerByName(self, name):
        costumer = self.costumers.findCostumersByName(name)
        if len(costumer) != 1:
            raise Exception(f"Costumer {name} was not found")
        return costumer[0]

    def searchCostumerName(self, name):
        return self.costumers.searchCostumerName(name)

    def searchBooksByTitle(self, title):
        return self.books.searchBooksByTitle(title)

    def getCostumersDict(self):
        return self.costumers.getCostumersDict()

    def getBooksDict(self):
        return self.books.getDictBooks()

    def getAuthorsDict(self):
        return self.books.getDictAuthors()

def resetBookStore(tag="testDev_"):
    bs0 = BookStore(tag, False)
##    bs0 = BookStore("test_")
    bs0.registerAuthor("Andre", "PT", True)
    bs0.registerAuthor("Bob", "PT", True)
    bs0.registerAuthor("Charlie", "US", False)
    
    bs0.registerBook("Tea", 200, "vol 1", "andre")
    bs0.registerBook("Tea2", 500, "vol 12", "andre")
    bs0.registerBook("mah name", 2200, "vol 31", "Bob")
    bs0.registerBook("eh jeff", 2200, "vol 31", "Charlie")
    
    bs0.registerCostumer("andre s", "01-01-2001")
    bs0.registerCostumer("Barkley", "01-10-2011")
    bs0.registerCostumer("Cat", "01-01-1990")
    bs0.registerPurchaseByName("andre s", ["1"], 200, 200)
    bs0.registerPurchaseByName("andre s", ["1"], 200, 200)
    bs0.registerPurchaseByName("cat", ["4"], 200, 200)
    return bs0
    


if __name__ == "__main__":
    resetBookStore()
    
