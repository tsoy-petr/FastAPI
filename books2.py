from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(max_length=100, min_length=1)
    description: Optional[str] = Field(title = "Description of the book",
                             max_length=100,
                             min_length=1)
    rating: int = Field(gt=-1, lt = 101)

BOOKS = []

@app.get("/")
async def read_all_books():
    return BOOKS

@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book