from typing import Generator, Any

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from database import Base
from dependencies import get_db
from middleware import MyMiddleware
from routers import authors, books
from tests.utils.test_settings_database import SessionTesting, engine


def start_application():
    app = FastAPI()
    app.include_router(authors.router)
    app.include_router(books.router)
    app.add_middleware(MyMiddleware)
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
        yield db_session

    app.dependency_overrides[get_db] = _get_test_db

    with TestClient(app) as client:
        client.headers = {"Authorization": "w2x7m_grd7m42k7(2@_^tv*pll^-l&242-@*d_b*pzs6-vy@-"}
        yield client
