from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dependencies import settings

if settings.TESTING:
    engine = create_engine(settings.DATABASE_URL)
else:
    engine = create_engine(settings.TEST_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
