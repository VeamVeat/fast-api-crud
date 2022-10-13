from typing import List

from pydantic import BaseModel, Field, validator, PositiveInt

from schemas.book import BookResponse


class AuthorResponse(BaseModel):
    id: PositiveInt
    name: str | None = Field(default=None, max_length=150)
    age: PositiveInt
    books: List[BookResponse] = []

    class Config:
        orm_mode = True


class _AuthorSchema(BaseModel):
    name: str
    age: PositiveInt

    @validator('age')
    def age_must_be_over_18(cls, age):
        if age < 18:
            raise ValueError(f'you are under 18')
        return age


class AuthorCreate(_AuthorSchema):
    pass


class AuthorPutUpdate(_AuthorSchema):
    pass


class AuthorPatchUpdate(_AuthorSchema):
    name: str | None = Field(default=None, max_length=20)
    age: PositiveInt | None


class _ChangeCountBookToAuthor(BaseModel):
    book_id: PositiveInt


class AddBookToAuthor(_ChangeCountBookToAuthor):
    pass


class DeleteBookToAuthor(_ChangeCountBookToAuthor):
    pass
