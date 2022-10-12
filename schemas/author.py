from typing import Optional, List

from pydantic import BaseModel, Field, validator

from schemas.book import BookResponse


class AuthorResponse(BaseModel):
    id: int
    name: str | None = Field(default=None, max_length=150)
    age: Optional[int]
    books: List[BookResponse] = []

    class Config:
        orm_mode = True


class AuthorUpdate(BaseModel):
    name: str | None = Field(default=None, max_length=20)
    age: Optional[int]

    @validator('age')
    def age_must_be_over_18(cls, age):
        if age < 18:
            raise ValueError(f'you are under 18')
        return age


class AuthorOptionalUpdate(AuthorUpdate):
    name: Optional[str] = None
    age: Optional[int] = None
