from typing import TYPE_CHECKING, List, Optional
from sqlmodel import SQLModel, Field, Column,Relationship
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime, date

class BookTag(SQLModel, table=True):
    __tablename__ = "booktags"
    book_id: uuid.UUID = Field(default=None, foreign_key="books.uid", primary_key=True)
    tag_id: uuid.UUID = Field(default=None, foreign_key="tags.uid", primary_key=True)

