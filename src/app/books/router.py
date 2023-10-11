from fastapi import APIRouter
from . import service, schemas, constants, models
from app.database import get_db
from datetime import datetime
books_router = APIRouter(prefix="/books")

@books_router.post("")
def create_book(book: schemas.Book):
    db = next(get_db())
    db_book = models.Book(title=book.title, author=book.author, publication_date=book.publication_date, created_at=datetime.now())
    created_book = service.create_book(db, db_book)
    return {"message": constants.SUCCESSFUL_BOOK_CREATION, "data": created_book }


@books_router.get("")
def get_books():
    db = next(get_db())
    books = service.get_books(db)
    return {"message": constants.SUCCESSFUL_BOOK_RETRIEVAL, "data": books}
