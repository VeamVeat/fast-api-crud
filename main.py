from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
import uvicorn
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from dependencies import get_db
from middleware import MyMiddleware
from schemas.book import Book as SchemaBook
from schemas.author import Author as SchemaAuthor
from schemas.author import AuthorUpdate as SchemaAuthorUpdate
from schemas.book import BookUpdate as SchemaBookUpdate
from models import Book as ModelBook
from models import Author as ModelAuthor

app = FastAPI()

my_middleware = MyMiddleware()
app.add_middleware(BaseHTTPMiddleware, dispatch=my_middleware)


@app.get('/book/')
async def book(db: Session = Depends(get_db)):
    book_list = db.query(ModelBook).all()
    return book_list


@app.post('/book/', response_model=SchemaBook, status_code=status.HTTP_201_CREATED)
async def book(book: SchemaBook, db: Session = Depends(get_db)):
    db_book = ModelBook(
        title=book.title,
        rating=book.rating,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    return db_book


@app.put("/book/{id}", response_model=SchemaBook)
async def book(id: int, book_schemas: SchemaBookUpdate, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(id)

    if not book_obj:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    else:
        book_obj.title = book_schemas.title
        book_obj.rating = book_schemas.rating
        db.commit()

    return book_obj


@app.delete("/book/{id}", response_model=SchemaBook)
async def book(id: int, db: Session = Depends(get_db)):
    book_obj = db.query(ModelBook).get(id)

    if not book_obj:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    else:
        db.delete(book_obj)
        db.commit()

    return book_obj


@app.get('/author/')
async def author(db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).all()
    return author_obj


@app.post('/author/', response_model=SchemaAuthor)
async def author(author_schemas: SchemaAuthorUpdate, db: Session = Depends(get_db)):
    db_author = ModelAuthor(
        name=author_schemas.name,
        age=author_schemas.age
    )
    db.add(db_author)
    db.commit()
    return db_author


@app.put("/author/{id}", response_model=SchemaAuthor)
async def author(id: int, author_schemas: SchemaAuthor, db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).get(id)

    if not author_obj:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    else:
        author_obj.name = author_schemas.name
        author_obj.age = author_schemas.age
        db.commit()

    return author_obj


@app.delete("/author/{id}", response_model=SchemaAuthor)
async def author(id: int, db: Session = Depends(get_db)):
    author_obj = db.query(ModelAuthor).get(id)

    if not author_obj:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    else:
        db.delete(author_obj)
        db.commit()

    return author_obj


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
