from typing import Union

from fastapi import Query
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True


class BookUpdate(BaseModel):
    title: Union[str, None] = Query(default=None, max_length=20)
    rating: int
