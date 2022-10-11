from pydantic import BaseSettings, PostgresDsn, Field


class Settings(BaseSettings):
    AUTHORIZATION: str

    DB_USERNAME: str
    DB_PASSWORD: str
    DB_DATABASE: str
    DB_HOST: str
    DB_PORT: str

    DATABASE_URL: PostgresDsn = Field(..., env="DATABASE_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
