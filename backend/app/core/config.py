"""This file : manages application configuration settings using environment variables. It uses the Pydantic library to define and validate these settings. This is used to centralize configuration management and make it easy to change settings without modifying the codebase directly. Unlike os.environ, Pydantic provides type validation and default values for settings.
"""


# importing BaseSettings from pydantic_settings to manage application settings using environment variables.
from pydantic_settings import BaseSettings

# Defining a Settings class that inherits from BaseSettings to manage application configuration.
class Settings(BaseSettings):
    # Environment Variables
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    # Algorithm used for signing the JWTs. Default is HS256 (HMAC with SHA-256).
    JWT_ALGORITHM: str = "HS256"
    # Access token expiration time in minutes. Default is 60 minutes.
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"   # Load variables from .env file
        env_file_encoding = "utf-8"


# Create a settings instance to import everywhere
settings = Settings()
