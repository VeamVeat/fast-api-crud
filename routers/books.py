from typing import List

from fastapi import Depends, HTTPException, status, APIRouter
from pydantic import PositiveInt
from sqlalchemy.orm import Session

from dependencies import get_db
from schemas.book import (
    BookResponse,
    BookPutUpdate,
    BookPatchUpdate,
    BookCreate
)
from models import Book as ModelBook

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.get("/", response_model=List[BookResponse])
async def get_books(db: Session = Depends(get_db)):
    return db.query(ModelBook).all()


@router.get("/{book_id}", response_model=BookResponse)
async def get_book_by_id(book_id: PositiveInt, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(book_id)

    if book_obj is None:
        raise HTTPException(
            status_code=404,
            detail=f"book item with id {book_id} not found"
        )

    return book_obj


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookCreate, db: Session = Depends(get_db)):
    book_data = book_data.dict(exclude_unset=True)
    db_book = ModelBook(**book_data)

    db.add(db_book)
    db.commit()
    return db_book


@router.put("/{book_id}", response_model=BookResponse)
async def update_book_by_id(book_id: PositiveInt, book_data: BookPutUpdate, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(book_id)

    if book_obj is None:
        raise HTTPException(
            status_code=404,
            detail=f"book item with id {book_id} not found"
        )

    book_data = book_data.dict()
    for key, value in book_data.items():
        setattr(book_obj, key, value)

    db.commit()

    return book_obj


@router.patch("/{book_id}", response_model=BookResponse)
async def optional_update_book_by_id(book_id: PositiveInt, book_data: BookPatchUpdate, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(book_id)

    if book_obj is None:
        raise HTTPException(
            status_code=404,
            detail=f"book item with id {book_id} not found"
        )

    book_data = book_data.dict(exclude_unset=True)
    for key, value in book_data.items():
        setattr(book_obj, key, value)

    db.commit()

    return book_obj


@router.delete("/{book_id}", response_model=BookResponse)
async def delete_book_by_id(book_id: PositiveInt, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(book_id)

    if book_obj is None:
        raise HTTPException(
            status_code=404,
            detail=f"book item with id {book_id} not found"
        )

    db.delete(book_obj)
    db.commit()

    return book_obj
