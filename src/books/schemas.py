from pydantic import BaseModel, Field
from typing import List, Optional
import uuid


# schema for creating a book(POST)
class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    price: float


#  Schema for updating a book (PUT / PATCH)
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
    price: Optional[float] = None


#  Schema for response (GET)
class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    price: float