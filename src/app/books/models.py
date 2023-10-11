from sqlalchemy import Column, Integer, String, DateTime, Date

from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    author = Column(String(50))
    publication_date = Column(Date, default=None)
    created_at = Column(DateTime, default=None)

