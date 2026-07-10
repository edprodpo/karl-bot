from dataclasses import dataclass

from src.services.exceptions.base import ServiceException


@dataclass(eq=False)
class AIBadRequestException(ServiceException):
    error: str

    @property
    def message(self) -> str:
        return f'Произошла ошибка при запросе к ИИ. "{self.error}"'
