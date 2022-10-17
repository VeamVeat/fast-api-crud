from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from dependencies import get_db
from middleware import MyMiddleware
from models import Author, Book
from routers import authors, books
from schemas.author import AuthorCreate
from schemas.book import BookCreate
from tests import fixtures
from tests.helpers.walk_packages import get_package_paths_in_module
from dependencies import settings
from tests.utils.test_settings_database import engine, SessionTesting

pytest_plugins = [*get_package_paths_in_module(fixtures)]


def create_item(db_session: SessionTesting, item: BaseModel, db_model):
    db_item = db_model(**item.dict())
    db_session.add(db_item)
    db_session.commit()
    db_session.refresh(db_item)
    return db_item

@pytest.fixture
def create_author(db_session: SessionTesting):
    a = create_item(
        db_session,
        AuthorCreate(
            name=settings.TEST_NAME_AUTHOR,
            age=settings.TEST_AGE_AUTHOR
        ),
        Author
    )
    return a


@pytest.fixture
def create_book(db_session: SessionTesting):
    create_item(
        db_session,
        BookCreate(
            title=settings.TEST_TITLE_BOOK,
            rating=settings.TEST_RATING_BOOK
        ),
        Book
    )
