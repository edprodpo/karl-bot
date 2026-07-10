
from pydantic import Field
from pydantic_settings import BaseSettings


class N8NSettings(BaseSettings):
    N8N_URL: str | None = Field(default=None)
