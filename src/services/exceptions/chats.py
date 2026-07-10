from dataclasses import dataclass

from src.services.exceptions.base import ServiceException


@dataclass(eq=False)
class ChatExistException(ServiceException):
    chat_id: int

    @property
    def message(self) -> str:
        return f'Чат с таким ID {self.chat_id} уже существует.'


@dataclass(eq=False)
class ChatNotFoundException(ServiceException):
    chat_id: int

    @property
    def message(self) -> str:
        return f'Чат с таким ID {self.chat_id} не найден.'


@dataclass(eq=False)
class ChatAccessException(ServiceException):
    chat_id: int

    @property
    def message(self) -> str:
        return f'У чата {self.chat_id} нет разрешения.'
