from factory.base import Factory
from factory.faker import Faker

from src.domain.entities.messages import Message


class MessageFactory(Factory):
    request: str = Faker('text')
    response: str = Faker('text')

    class Meta:
        model = Message
