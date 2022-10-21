from typing import Generator, Any

import pytest
from fastapi import FastAPI

from tests.utils.test_settings_database import engine, SessionTesting


@pytest.fixture(scope="class")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()
