from sqlmodel import Session, select
from src.books.models import Book
from src.books.schemas import BookCreate, BookUpdate


# CREATE BOOK
def create_book(session: Session, book_data: BookCreate):
    book = Book(**book_data.dict())
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


# GET ALL BOOKS
def get_books(session: Session):
    statement = select(Book)
    return session.exec(statement).all()


# UPDATE BOOK
def update_book(session: Session, book_id, book_data: BookUpdate):
    book = session.get(Book, book_id)
    if not book:
        return None

    for key, value in book_data.dict(exclude_unset=True).items():
        setattr(book, key, value)

    session.add(book)
    session.commit()
    session.refresh(book)
    return book


# DELETE BOOK
def delete_book(session: Session, book_id):
    book = session.get(Book, book_id)
    if not book:
        return False

    session.delete(book)
    session.commit()
    return True
