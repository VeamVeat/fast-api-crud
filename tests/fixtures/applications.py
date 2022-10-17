from typing import Generator, Any

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from database import Base
from dependencies import get_db
from routers import authors, books
from tests.utils.test_settings_database import SessionTesting, engine


def start_application():
    app = FastAPI()
    app.include_router(authors.router)
    app.include_router(books.router)
    # app.add_middleware(MyMiddleware)
    return app


@pytest.fixture()
def app() -> Generator[FastAPI, Any, None]:

    Base.metadata.create_all(engine)
    _app = start_application()
    yield _app
    Base.metadata.drop_all(engine)


@pytest.fixture()
def client(
        app: FastAPI, db_session: SessionTesting
) -> Generator[TestClient, Any, None]:

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client
