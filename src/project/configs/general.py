import enum
from zoneinfo import ZoneInfo

from pydantic_settings import BaseSettings


class Environment(str, enum.Enum):
    DEV = 'dev'
    PROD = 'prod'
    LOCAL = 'local'


class GeneralSettings(BaseSettings):
    GENERAL_PORT: int
    GENERAL_PROXY: str
    TIME_ZONE: ZoneInfo = ZoneInfo('Europe/Moscow')
    ENVIRONMENT: Environment = Environment.LOCAL
