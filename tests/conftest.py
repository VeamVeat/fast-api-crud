from typing import Generator

import pytest
from fastapi.testclient import TestClient

import tests.fixtures
from fast_api_crud.dependencies import get_db
from fast_api_crud.database import Base
from fast_api_crud.main import app
from tests.utils.overrides import override_get_db
from tests.utils.test_db import TestingSessionLocal, engine
from tests.helpers.walk_packages import get_package_paths_in_module
import os

import pytest
from alembic import command
from alembic.config import Config
from app.models import database
from sqlalchemy_utils import create_database, drop_database

pytest_plugins = [*get_package_paths_in_module(tests.fixtures)]

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session")
def db() -> Generator:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    yield TestingSessionLocal()


@pytest.fixture(scope="module")
def temp_db():
    create_database(database.TEST_SQLALCHEMY_DATABASE_URL)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    alembic_cfg = Config(os.path.join(base_dir, "alembic.ini"))
    command.upgrade(alembic_cfg, "head")
    try:
        yield database.TEST_SQLALCHEMY_DATABASE_URL
    finally:
        drop_database(database.TEST_SQLALCHEMY_DATABASE_URL)


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
