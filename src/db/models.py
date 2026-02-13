from sqlmodel import Relationship, SQLModel,Field,Column
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime
from typing import Optional, List
from booktag.models import BookTag
from src.books.models import Book
from src.users.models import User
class Review(SQLModel,table =True):
    __tablename__ = "reviews"
    uid:uuid.UUID= Field(
        sa_column =Column(pg.UUID,nullable=False,primary_key =True,default=uuid.uuid4))
    rating: int 
    review_text :str= Field(sa_column=Column(pg.VARCHAR,nullable=False))
    user_uid:Optional[uuid.UUID]=Field(default=None,foreign_key="users.uid")
    book_uid:Optional[uuid.UUID]=Field(default=None,foreign_key="books.uid")
    creates_at: datetime =Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    updated_at: datetime =Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now))
    user: Optional[User]=Relationship(back_populates="reviews")
    book: Optional[Book]=Relationship(back_populates="reviews")

class Tag(SQLModel, table=True):
    __tablename__ = "tags"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    name: str = Field(sa_column=Column(pg.VARCHAR, nullable=False))
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    books: list["Book"] = Relationship(
        back_populates="tags",
        link_model=BookTag
    )

    def __repr__(self) -> str:
        return f"<Tag {self.name}>"    