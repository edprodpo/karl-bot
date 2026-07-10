from uuid import uuid4

from factory.base import Factory
from factory.faker import Faker

from src.domain.entities.users import User


class UserFactory(Factory):
    vk_id: int = Faker('random_int', min=0)
    email: str = Faker('email')
    name: str = Faker('name', locale='ru_RU')
    thread_id: str = str(uuid4())

    class Meta:
        model = User
