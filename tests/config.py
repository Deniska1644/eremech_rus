import os
from pydantic_settings import BaseSettings, SettingsConfigDict

env_file = os.path.join(os.path.dirname(os.getcwd()), '.env')


class Settings(BaseSettings):

    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    APP_HOST:str
    APP_PORT:str

    model_config = SettingsConfigDict(env_file='.env')

    def get_pg_url(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()

