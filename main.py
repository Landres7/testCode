from typing import Union, List

from fastapi import FastAPI

from BookStore import BookStore, resetBookStore
bookStore = BookStore("testDev_", True)
try:
    bookStore = BookStore("testDev_", True)
except:
    bookStore = resetBookStore("testDev_")

app = FastAPI()

def exceptionHandler(e):
    bookStore.saveState()
    
    return {"msg": "Error: "+str(e)}


@app.get("/Reset")
def restState(newTag:str = None):
    try:
        newTag = "testDev_" if not newTag else newTag
        bookStore = resetBookStore(newTag)
        return {"msg":"Success"}
    except Exception as e:
        return {"msg": "Error: "+str(e)} 

@app.get("/cleanBooksList")
def cleanAllBooks():
    try:
        bookStore.books.clearBookList()
        return {"msg":"Success"}
    except Exception as e:
        return {"msg": "Error: "+str(e)} 


@app.post("/purchase")
def registerPurchase(costumerName:str, itemPurchased:str, price:float, payed:float):
    try:
        if bookStore.registerPurchaseByName(costumerName, [itemPurchased], price, payed):
            return {"msg":"Success"}
        return {"msg": "Error - Unknown Error"}
    except Exception as e:
        return exceptionHandler(e)


@app.post("/purchase/{cname}")
def registerPurchaseByTitle(cname:str, title:str, price:float, payed:float):
    
    try:
        if bookStore.registerPurchaseByTitle(cname, title, price, payed):
            return {"msg":"Success"}
        return {"msg":"Error - Unknown"}
    except Exception as e:
        return exceptionHandler(e)


@app.post("/customers")
def registerCostumer(name:str, dob:str):
    try:
        if bookStore.registerCostumer(name, dob):
            return {"msg":"Success"}
        return {"msg":"Error - Unknown"}

    except Exception as e:
        return exceptionHandler(e)

@app.post("/authors")
def addAuthor(name:str, nationality:str,  alive:bool):
    try:
        if bookStore.registerAuthor(name, nationality, alive):
            return {"msg":"Success"}
        return {"msg": "Error - Author name already exists"}
    except Exception as e:
        return exceptionHandler(e)


@app.post("/books")
def addBook(title:str, authorName:str, volume:str, numPages:int):
    try:
        if bookStore.registerBook(title, numPages, volume, authorName):
            return {"msg":"Success"}
        return {"msg":"Error - Book Title already exists"}
    except Exception as e:
        return exceptionHandler(e)

@app.get("/customers")
def getAllCostumers():
    try:
        return bookStore.getCostumers()

    except Exception as e:
        return exceptionHandler(e)




@app.get("/customers/{cname}")
def searchCostumerName(cname:str):
    try:
        return bookStore.searchCostumerName(cname)
            
    except Exception as e:
        return exceptionHandler(e)

@app.get("/authors")
def getAllAuthors():
    try:
        
        return bookStore.getAuthorsDict()
    except Exception as e:
        return exceptionHandler(e)



@app.get("/authors/{authorId}")
def getAuthorById(authorId:str):
    try:
        return {"authors":
                        list(filter(lambda a: a["authorId"] == authorId,
                                    bookStore.getAuthorsDict()["authors"]))}
    except Exception as e:
        return exceptionHandler(e)


    
@app.get("/books")
def getAllBooks():
    try:
        
        return bookStore.getBooksDict()
    except Exception as e:
        return exceptionHandler(e)

@app.get("/books/{title}")
def searchBooksByTitle(title):
    try:
        
        return  bookStore.searchBooksByTitle(title)
    
    except Exception as e:
        return exceptionHandler(e)




@app.get("/")
def read_root():
    return {"Hello": "World!"}
@app.get("/hey")
def read_root():
    return "hello! How are you?"

