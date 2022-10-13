from pydantic import BaseSettings, PostgresDsn, validator, PositiveInt


class Settings(BaseSettings):
    AUTHORIZATION: str

    DB_USERNAME: str
    DB_PASSWORD: str
    DB_DATABASE: str
    DB_HOST: str
    DB_PORT: PositiveInt

    DATABASE_URL: PostgresDsn

    @validator('DATABASE_URL')
    def connection_db(cls, database_url, values):
        database_url = f"postgresql://{values.get('DB_USERNAME')}:" \
                       f"{values.get('DB_PASSWORD')}@{values.get('DB_HOST')}:" \
                       f"{values.get('DB_PORT')}/{values.get('DB_DATABASE')}"
        return database_url

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
