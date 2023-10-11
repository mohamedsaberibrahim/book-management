from pydantic import BaseModel


class Book(BaseModel):
    title: str
    publication_date: str
    author: str
