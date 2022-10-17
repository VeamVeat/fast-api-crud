from typing import List

from fastapi import Depends, HTTPException, status, APIRouter
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


@router.get("/all", response_model=List[AuthorResponse])
async def get_authors(db: Session = Depends(get_db)):
    return db.query(ModelAuthor).all()


@router.get("/{author_id}", response_model=AuthorResponse)
async def get_author_by_id(author_id: PositiveInt, db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).get(author_id)

    if author_obj is None:
        raise HTTPException(status_code=404, detail=f"author item with id {author_id} not found")

    return author_obj


@router.post("/", response_model=AuthorResponse, status_code=status.HTTP_201_CREATED)
async def create_author(author_data: AuthorCreate, db: Session = Depends(get_db)):
    author_data = author_data.dict()
    db_author = ModelAuthor()

    for key, value in author_data.items():
        setattr(db_author, key, value)

    db.add(db_author)
    db.commit()
    return db_author


@router.put("/{author_id}", response_model=AuthorResponse)
async def update_author(author_id: PositiveInt, author_data: AuthorPutUpdate, db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).get(author_id)

    if author_obj is None:
        raise HTTPException(status_code=404, detail=f"author item with id {author_id} not found")

    author_data = author_data.dict()
    for key, value in author_data.items():
        setattr(author_obj, key, value)

    db.commit()

    return author_obj


@router.patch("/{author_id}", response_model=AuthorResponse)
async def optional_update_author_by_id(
        author_id: PositiveInt,
        author_data: AuthorPatchUpdate,
        db: Session = Depends(get_db)
):
    author_obj = db.query(ModelAuthor).get(id)

    if author_obj is None:
        raise HTTPException(status_code=404, detail=f"author item with id {author_id} not found")

    author_data = author_data.dict(exclude_unset=True)
    for key, value in author_data.items():
        setattr(author_obj, key, value)

    db.commit()

    return author_obj


@router.post("/{author_id}", response_model=AuthorResponse)
async def add_book_to_author_id(author_id: PositiveInt, add_book_data: AddBookToAuthor, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(add_book_data.book_id)
    author_obj = db.query(ModelAuthor).get(author_id)

    if author_obj is None or book_obj is None:
        raise HTTPException(status_code=404, detail=f"item with id {author_id} not found")

    author_obj.books.append(book_obj)
    db.commit()

    return author_obj


@router.delete("/{author_id}", response_model=AuthorResponse)
async def delete_book_to_author_id(
        author_id: PositiveInt,
        delete_book_data: DeleteBookToAuthor,
        db: Session = Depends(get_db)
):
    book_obj = db.query(ModelBook).get(delete_book_data.book_id)
    author_obj = db.query(ModelAuthor).get(author_id)

    if author_obj is None or book_obj is None:
        raise HTTPException(status_code=404, detail=f"item with id {author_id} not found")

    author_obj.books.delete(book_obj)
    db.commit()

    return author_obj


@router.delete("/{author_id}", response_model=AuthorResponse)
async def delete_author(author_id: PositiveInt, db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).get(author_id)

    if author_obj is None:
        raise HTTPException(status_code=404, detail=f"author item with id {author_id} not found")

    db.delete(author_obj)
    db.commit()

    return author_obj
