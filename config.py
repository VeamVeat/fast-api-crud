import os

from pydantic import BaseSettings, PostgresDsn, validator, PositiveInt


class Settings(BaseSettings):
    AUTHORIZATION: str

    DB_USERNAME: str
    DB_PASSWORD: str
    DB_DATABASE: str
    DB_HOST: str
    DB_PORT: PositiveInt

    DATABASE_URL: PostgresDsn
    TEST_DATABASE_URL: str = os.getenv("TEST_DATABASE_URL")

    @validator("DATABASE_URL")
    def connection_db(cls, database_url, values):
        db_username = values.get("DB_USERNAME")
        db_password = values.get("DB_PASSWORD")
        db_host = values.get("DB_HOST")
        db_port = values.get("DB_PORT")
        db_database = values.get("DB_DATABASE")

        database_url = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_database}"
        return database_url

    class Config:
        env_file = "env_project/.env"
        env_file_encoding = "utf-8"
