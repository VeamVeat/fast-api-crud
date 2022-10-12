from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import uvicorn
from fastapi import FastAPI

from dependencies import get_db
from middleware import MyMiddleware
from schemas.book import BookResponse, BookUpdate
from schemas.author import AuthorResponse, AuthorUpdate
from models import Book as ModelBook
from models import Author as ModelAuthor

app = FastAPI()

# app.add_middleware(MyMiddleware)


@app.get('/book/', response_model=List[BookResponse])
async def get_books(db: Session = Depends(get_db)):
    return db.query(ModelBook).all()


@app.get("/book/{id}", response_model=BookResponse)
async def get_book_by_id(id: int, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(id)

    if not book_obj:
        raise HTTPException(status_code=403, detail=f"book item with id {id} not found")

    return book_obj


@app.post('/book/', response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookUpdate, db: Session = Depends(get_db)):
    db_book = ModelBook(
        title=book.title,
        rating=book.rating
    )
    db.add(db_book)
    db.commit()
    return db_book


@app.put("/book/{id}", response_model=BookResponse)
async def update_book_by_id(id: int, book_schema: BookUpdate, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(id)

    if not book_obj:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    book_obj.title = book_schema.title
    book_obj.rating = book_schema.rating
    db.commit()

    return book_obj


@app.delete("/book/{id}", response_model=BookResponse)
async def delete_book_by_id(id: int, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(id)

    if not book_obj:
        raise HTTPException(status_code=404, detail=f"book item with id {id} not found")

    db.delete(book_obj)
    db.commit()

    return book_obj


@app.get('/author/', response_model=List[AuthorResponse])
async def get_authors(db: Session = Depends(get_db)):
    return db.query(ModelAuthor).all()


@app.get("/author/{id}", response_model=AuthorResponse)
async def get_author_by_id(id: int, db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).get(id)

    if not author_obj:
        raise HTTPException(status_code=404, detail=f"author item with id {id} not found")

    return author_obj


@app.post('/author/', response_model=AuthorResponse, status_code=status.HTTP_201_CREATED)
async def create_author(author_schema: AuthorUpdate, db: Session = Depends(get_db)):
    db_author = ModelAuthor(
        name=author_schema.name,
        age=author_schema.age
    )
    db.add(db_author)
    db.commit()
    return db_author


@app.put("/author/{id}", response_model=AuthorResponse)
async def update_author(id: int, author_schema: AuthorUpdate, db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).get(id)

    if not author_obj:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    author_obj.name = author_schema.name
    author_obj.age = author_schema.age
    db.commit()

    return author_obj


@app.delete("/author/{id}", response_model=AuthorResponse)
async def delete_author(id: int, db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).get(id)

    if not author_obj:
        raise HTTPException(status_code=404, detail=f"author item with id {id} not found")

    db.delete(author_obj)
    db.commit()

    return author_obj


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
