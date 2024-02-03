from typing import Union, List

from fastapi import FastAPI

from Books import getBooksSavedState

bookList = getBooksSavedState()

app = FastAPI()

def exceptionHandler(e):
    bookList._saveState()
    
    return {"msg": "Error: "+str(e)}

@app.get("/cleanBooksList")
def cleanAllBooks():
    try:
        bookList.clearBookList()
        return {"msg":"Success"}
    except Exception as e:
        return {"msg": "Error: "+str(e)} 


@app.get("/authors")
def getAllAuthors():
    try:
        
        return bookList.getDictAuthors()
    except Exception as e:
        return exceptionHandler(e)

@app.get("/authors/<authorId>")
def getAuthorById(authorId:str):
    try:
        return {"authors":
                        list(filter(lambda a: a["authorId"] == authorId,
                                    bookList.getDictAuthors()["authors"]))}
    except Exception as e:
        return exceptionHandler(e)
@app.get("/books")
def getAllBooks():
    try:
        
        return bookList.getDictBooks()
    except Exception as e:
        return exceptionHandler(e)

@app.post("/books")
def addBook(title:str, authorName:str, volume:str, numPages:int):
    try:
        if bookList.addBook(title, numPages, volume, authorName):
            return {"msg":"Success"}
        return {"msg":"Error - Book Title already exists"}
    except Exception as e:
        return exceptionHandler(e)

@app.get("/")
def read_root():
    return {"Hello": "World!"}
@app.get("/hey")
def read_root():
    return "hello! How are you?"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

