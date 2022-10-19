import pytest

from models import Author, Book
from schemas.author import AuthorCreate
from schemas.book import BookCreate
from tests import fixtures
from tests.helpers.walk_packages import get_package_paths_in_module
from config import settings
from tests.test_services import TestBaseService
from tests.utils.test_settings_database import SessionTesting

pytest_plugins = [*get_package_paths_in_module(fixtures)]


@pytest.fixture
def create_author(db_session: SessionTesting):
    author_schema = AuthorCreate(
        name=settings.TEST_NAME_AUTHOR,
        age=settings.TEST_AGE_AUTHOR
    )
    base_service = TestBaseService(db_session, author_schema, Author)
    author_obj = base_service.create_item()
    return author_obj


@pytest.fixture
def create_book(db_session: SessionTesting):
    book_schema = BookCreate(
        title=settings.TEST_TITLE_BOOK,
        rating=settings.TEST_RATING_BOOK
    )
    base_service = TestBaseService(db_session, book_schema, Book)
    book_obj = base_service.create_item()
    return book_obj
