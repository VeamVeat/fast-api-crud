from pydantic import BaseModel, StrictStr, Field, validator


class Author(BaseModel):
    id: int
    name: str
    age: str

    class Config:
        orm_mode = True


class AuthorUpdate(BaseModel):
    name: StrictStr = Field(min_length=1, max_length=50)
    age: int

    @validator('age')
    def age_must_be_over_18(cls, age):
        if age < 18:
            raise ValueError(f'you are under 18')
        return age
