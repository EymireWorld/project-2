from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='db.env', env_file_encoding='utf-8')

    host: str = Field(validation_alias='postgres_host')
    db: str = Field(validation_alias='postgres_db')
    user: str = Field(validation_alias='postgres_user')
    password: str = Field(validation_alias='postgres_password')


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='app.env', env_file_encoding='utf-8')
    
    jwt_token_lifetime: int  # In minutes


database_settings = DatabaseSettings()  # type: ignore
app_settings = AppSettings()  # type: ignore
