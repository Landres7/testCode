from typing import Union

from fastapi import FastAPI

from Books import getBooksSavedState

bookList = getBooksSavedState()

app = FastAPI()

@app.get("/books")
def getAllBooks():
    return {"books":bookList}

@app.get("/")
def read_root():
    return {"Hello": "World!"}
@app.get("/hey")
def read_root():
    return "hello! How are you?"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

