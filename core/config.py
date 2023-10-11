import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class Settings(BaseSettings):
    DB_USERNAME:str = os.environ.get("DB_USERNAME")
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_PASSWORD: str | None = os.environ.get("DB_PASSWORD") or None
    DB_PORT: str = os.environ.get("DB_PORT")
    # DB url create
    DATABASE_URL: str = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# export setting from a function
def getSettings()-> Settings:
    return Settings()