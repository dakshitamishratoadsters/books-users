from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Column,Relationship
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime, date
if TYPE_CHECKING:
  from src.db.models import Review
  from src.users.models import User
  from src.db.models import Tag,BookTag
from booktag.models import BookTag




class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
            pg.UUID(as_uuid=True),
            primary_key=True,
            unique=True,
            nullable=False
        )
    )

    title: str = Field(nullable=False)
    author: str = Field(nullable=False)
    publisher: str = Field(nullable=False)
    published_date: date = Field(nullable=False)
    page_count: int = Field(nullable=False)
    language: str = Field(nullable=False)
    price: float = Field(nullable=False)
    # add this line below
    user_uid:Optional[uuid.UUID]= Field(default=None,foreign_key="users.uid")

    reviews: List["Review"] = Relationship(
        back_populates="book", sa_relationship_kwargs={"lazy": "selectin"}
    )

    tags: list["Tag"] = Relationship(
        back_populates="books",
        link_model=BookTag
    )

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(pg.TIMESTAMP, default=datetime.utcnow)
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(pg.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    )
    user:Optional["User"]=Relationship(back_populates="books")

    def __repr__(self) -> str:
        return f"<Book {self.title}>"
