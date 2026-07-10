from pydantic import ConfigDict

from src.project.configs.admin import AdminSettings
from src.project.configs.general import GeneralSettings
from src.project.configs.logger import LoggingSettings
from src.project.configs.n8n import N8NSettings
from src.project.configs.openai import OpenAISettings
from src.project.configs.vk import VKSettings


class Settings(
    AdminSettings,
    LoggingSettings,
    GeneralSettings,
    VKSettings,
    OpenAISettings,
    N8NSettings,
):
    model_config = ConfigDict(
        case_sensitive=True,
        env_file=".env",
    )


settings = Settings()
