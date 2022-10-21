from pydantic import BaseModel, Field, PositiveInt


class BookResponse(BaseModel):
    id: PositiveInt
    title: str | None = Field(default=None, max_length=20)
    rating: PositiveInt | None

    class Config:
        orm_mode = True


class BookDelete(BaseModel):
    book_id: PositiveInt


class _BookSchema(BaseModel):
    title: str
    rating: PositiveInt


class BookCreate(_BookSchema):
    author_id: PositiveInt | None


class BookPutUpdate(_BookSchema):
    pass


class BookPatchUpdate(_BookSchema):
    title: str | None = Field(default=None, max_length=20)
    rating: PositiveInt | None
