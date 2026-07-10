from dataclasses import dataclass

from src.services.exceptions.base import ServiceException


@dataclass(eq=False)
class HTTPClientException(ServiceException):
    status_code: int
    error: str

    @property
    def message(self) -> str:
        return f'Ошибка http клиента. {self.status_code} - "{self.error}".'
