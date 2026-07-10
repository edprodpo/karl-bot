from dataclasses import dataclass

from src.services.exceptions.base import ServiceException


@dataclass(eq=False)
class UserExistException(ServiceException):
    vk_id: int

    @property
    def message(self) -> str:
        return f'Пользователь с VK ID {self.vk_id} уже существует.'


@dataclass(eq=False)
class UserNotFoundException(ServiceException):
    vk_id: int

    @property
    def message(self) -> str:
        return f'Пользователь с VK ID {self.vk_id} не найден.'
