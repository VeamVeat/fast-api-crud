from fastapi import APIRouter
from typing import List

from fastapi import Depends, HTTPException, status
from pydantic import PositiveInt
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas.author import (
    AuthorResponse,
    AuthorPutUpdate,
    AuthorPatchUpdate,
    AuthorCreate,
    AddBookToAuthor,
    DeleteBookToAuthor
)
from models import Book as ModelBook
from models import Author as ModelAuthor

router = APIRouter(
    prefix="/author",
    tags=["authors"],
)


@router.get('/all', response_model=List[AuthorResponse])
async def get_authors(db: Session = Depends(get_db)):
    return db.query(ModelAuthor).all()


@router.get("/{id}", response_model=AuthorResponse)
async def get_author_by_id(id: PositiveInt, db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).get(id)

    if not author_obj:
        raise HTTPException(status_code=404, detail=f"author item with id {id} not found")

    return author_obj


@router.post('/', response_model=AuthorResponse, status_code=status.HTTP_201_CREATED)
async def create_author(author_schema: AuthorCreate, db: Session = Depends(get_db)):
    db_author = ModelAuthor(
        name=author_schema.name,
        age=author_schema.age
    )
    db.add(db_author)
    db.commit()
    return db_author


@router.put("/{id}", response_model=AuthorResponse)
async def update_author(id: PositiveInt, author_schema: AuthorPutUpdate, db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).get(id)

    if not author_obj:
        raise HTTPException(status_code=404, detail=f"author item with id {id} not found")

    author_obj.name = author_schema.name
    author_obj.age = author_schema.age
    db.commit()

    return author_obj


@router.patch("/{id}", response_model=AuthorResponse)
async def optional_update_author_by_id(
        id: PositiveInt,
        author_schema: AuthorPatchUpdate,
        db: Session = Depends(get_db)
):
    author_obj = db.query(ModelAuthor).get(id)

    if not author_obj:
        raise HTTPException(status_code=404, detail=f"author item with id {id} not found")

    author_data = author_schema.dict(exclude_unset=True)
    for key, value in author_data.items():
        setattr(author_obj, key, value)

    db.commit()

    return author_obj


@router.post("/{id}", response_model=AuthorResponse)
async def add_book_to_author_id(id: PositiveInt, add_book_schema: AddBookToAuthor, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(add_book_schema.book_id)
    author_obj = db.query(ModelAuthor).get(id)

    if not author_obj or not book_obj:
        raise HTTPException(status_code=404, detail=f"item with id {id} not found")

    author_obj.books.append(book_obj)
    db.commit()

    return author_obj


@router.delete("/{id}", response_model=AuthorResponse)
async def delete_book_to_author_id(
        id: PositiveInt,
        delete_book_schema: DeleteBookToAuthor,
        db: Session = Depends(get_db)
):
    book_obj = db.query(ModelBook).get(delete_book_schema.book_id)
    author_obj = db.query(ModelAuthor).get(id)

    if not author_obj or not book_obj:
        raise HTTPException(status_code=404, detail=f"item with id {id} not found")

    author_obj.books.delete(book_obj)
    db.commit()

    return author_obj


@router.delete("/{id}", response_model=AuthorResponse)
async def delete_author(id: PositiveInt, db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).get(id)

    if not author_obj:
        raise HTTPException(status_code=404, detail=f"author item with id {id} not found")

    db.delete(author_obj)
    db.commit()

    return author_obj
