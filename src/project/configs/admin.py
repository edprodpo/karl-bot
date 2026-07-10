from pydantic_settings import BaseSettings


class AdminSettings(BaseSettings):
    ADMIN_API_URL: str
    ADMIN_API_TOKEN: str
