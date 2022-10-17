from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dependencies import settings

SQLALCHEMY_DATABASE_URL = settings.TEST_DATABASE_URL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)
