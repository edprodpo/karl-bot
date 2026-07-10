from factory.base import Factory
from factory.faker import Faker

from src.domain.entities.chats import Chat


class ChatFactory(Factory):
    chat_id: int = Faker('random_int', min=0)
    title: str = Faker('text', max_nb_chars=52)

    class Meta:
        model = Chat
