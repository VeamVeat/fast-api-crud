import uvicorn

from fastapi import FastAPI

from middleware import MyMiddleware
from routers import authors
from routers import books


app = FastAPI()

app.include_router(authors.router)
app.include_router(books.router)
app.add_middleware(MyMiddleware)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
