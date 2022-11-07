from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    debug: bool = Field(default=False, env="DEBUG")
    secret_key: str = Field(
        default="Create the .env file, see .env-template!", env="SECRET_KEY"
    )
