import pytest

from dependencies import settings


@pytest.fixture()
def data_create_author():
    return {
        "name": settings.TEST_NAME_AUTHOR,
        "age": settings.TEST_AGE_AUTHOR
    }
