from pydantic import Field
from pydantic_settings import BaseSettings


class OpenAISettings(BaseSettings):
    OPENAI_API_KEY: str | None = Field(default=None)
    OPENAI_ASSISTANT_ID: str | None = Field(default=None)
