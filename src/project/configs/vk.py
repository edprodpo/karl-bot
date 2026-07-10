from pydantic_settings import BaseSettings


class VKSettings(BaseSettings):
    VK_API_KEY: str
    VK_BOT_KEYWORDS: list
