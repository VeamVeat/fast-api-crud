from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dependencies import get_db_settings

settings = get_db_settings()

DATABASE_URL = f"postgresql://{settings.username}:{settings.password}" \
               f"@{settings.host}:{settings.port}/{settings.database}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
