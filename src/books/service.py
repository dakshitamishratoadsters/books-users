import datetime
from typing import List, Optional
from sqlmodel import Session, select
from fastapi import HTTPException
from src.books.models import Book
from src.books.schemas import BookCreate, BookUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc


class BookService:
    """Service class for all book-related operations"""
    
    def create_book(self, session: Session, book_data: BookCreate, user_uid: str) -> Book:
        """Create a new book"""
        book = Book(**book_data.dict())
        book.user_uid = user_uid
        session.add(book)
        session.commit()
        session.refresh(book)
        return book
    
    def get_all_books(self, session: Session) -> List[Book]:
        """Get all books"""
        statement = select(Book)
        return session.exec(statement).all()
    
    def get_book_by_id(self, session: Session, book_id: str) -> Optional[Book]:
        """Get a single book by ID"""
        return session.get(Book, book_id)
    
    def update_book(self, session: Session, book_id: str, book_data: BookUpdate) -> Book:
        """Update an existing book"""
        book = session.get(Book, book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        
        for key, value in book_data.dict(exclude_unset=True).items():
            setattr(book, key, value)
        
        session.add(book)
        session.commit()
        session.refresh(book)
        return book
    
    def delete_book(self, session: Session, book_id: str) -> dict:
        """Delete a book"""
        book = session.get(Book, book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        
        session.delete(book)
        session.commit()
        return {"message": "Book deleted successfully"}
    
    async def get_user_books(self, user_uid: str, session: AsyncSession):
        statement = (
            select(Book)
            .where(Book.user_uid == user_uid)
            .order_by(desc(Book.created_at))
        )

        result = await session.exec(statement)

        return result.all()

    # async def create_book(
    #     self, book_data: BookCreate, user_uid: str, session: AsyncSession
    # ):
    #     book_data_dict = book_data.model_dump()

    #     new_book = Book(**book_data_dict)

    #     new_book.published_date = datetime.strptime(
    #         book_data_dict["published_date"], "%Y-%m-%d"
    #     )

    #     new_book.user_uid = user_uid

    #     session.add(new_book)

    #     await session.commit()

    #     return new_book



# Create a singleton instance for easy import
book_service = BookService()

