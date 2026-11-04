from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Windows Security Monitor"
    DEBUG: bool = True

settings = Settings()
