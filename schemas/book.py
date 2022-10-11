from typing import Optional
from pydantic import BaseModel, Field


class BookResponse(BaseModel):
    id: int
    title: str | None = Field(default=None, max_length=20)
    rating: Optional[int]

    class Config:
        orm_mode = True


class BookUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=20)
    rating: Optional[int]
