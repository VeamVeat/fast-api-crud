from typing import List

from fastapi import Depends, HTTPException, status, APIRouter
from pydantic import PositiveInt
from sqlalchemy.orm import Session

from dependencies import get_db
from schemas.book import BookResponse, BookPutUpdate, BookPatchUpdate, BookCreate
from models import Book as ModelBook

router = APIRouter(
    prefix="/book",
    tags=["books"],
)


@router.get('/all', response_model=List[BookResponse])
async def get_books(db: Session = Depends(get_db)):
    return db.query(ModelBook).all()


@router.get("/{id}", response_model=BookResponse)
async def get_book_by_id(id: PositiveInt, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(id)

    if not book_obj:
        raise HTTPException(status_code=404, detail=f"book item with id {id} not found")

    return book_obj


@router.post('/', response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    book_data = book.dict(exclude_unset=True)
    db_book = ModelBook(**book_data)

    db.add(db_book)
    db.commit()
    return db_book


@router.put("/{id}", response_model=BookResponse)
async def update_book_by_id(id: PositiveInt, book_schema: BookPutUpdate, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(id)

    if not book_obj:
        raise HTTPException(status_code=404, detail=f"book item with id {id} not found")

    book_obj.title = book_schema.title
    book_obj.rating = book_schema.rating
    db.commit()

    return book_obj


@router.patch("/{id}", response_model=BookResponse)
async def optional_update_book_by_id(id: PositiveInt, book_schema: BookPatchUpdate, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(id)

    if not book_obj:
        raise HTTPException(status_code=404, detail=f"book item with id {id} not found")

    book_data = book_schema.dict(exclude_unset=True)
    for key, value in book_data.items():
        setattr(book_obj, key, value)

    db.commit()

    return book_obj


@router.delete("/{id}", response_model=BookResponse)
async def delete_book_by_id(id: PositiveInt, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(id)

    if not book_obj:
        raise HTTPException(status_code=404, detail=f"book item with id {id} not found")

    db.delete(book_obj)
    db.commit()

    return book_obj
