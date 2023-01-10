from functools import lru_cache

from pydantic import BaseSettings, Field, validator


class Settings(BaseSettings):
    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'

    server_host: str = Field(default="localhost", env='server_host')
    server_port: int = Field(default="8000", env='server_port')

    currate_api_key: str = None

    access_token_expire_minutes: int = 30  # 30 min
    refresh_token_expire_minutes: int = 60 * 24 * 7  # 7 day
    algorithm: str = "HS256"
    jwt_secret_key: str = Field(
        default='M6cXd7qCIz8VJ1DLKHMQ_1NS_4QIjhshnV-ms7iIsl5652mf21MbKFer0x8XUFfc8lfgXUdnO98tufViKoVa6g',
        env='jwt_secret_key')
    jwt_refresh_secret_key: str = Field(
        default='KwxcZ4MuKm2dL0e8LZC9lPXGhyOjrD0REAZi2F6FFufZYYOXcJ5eQLzekEVZ2eymeaav4V4md_Qf29tWNJb_dw',
        env='jwt_refresh_secret_key')

@lru_cache()
def get_settings():
    return Settings()


setting = get_settings()
