import pytest

from dependencies import settings


@pytest.fixture()
def data_create_book():
    return {
        "title": settings.TEST_TITLE_BOOK,
        "rating": settings.TEST_RATING_BOOK
    }
