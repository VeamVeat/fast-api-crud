from functools import lru_cache

from sqlalchemy.orm import Session

import config


def get_db() -> Session:
    from database import SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@lru_cache
def get_db_settings() -> config.Settings:
    return config.Settings()


settings = get_db_settings()
