import pytest
from faker import Faker
from punq import Container

from src.services.chats.base import BaseChatService
from src.services.clients.ai_clients.base import BaseAIClient
from src.services.clients.http_clients.base import BaseHTTPClient
from src.services.messages.base import BaseMessageService
from src.services.users.base import BaseUserService
from src.services.vk_service.base import BaseVKService
from src.tests.fixtures import init_dummy_container


@pytest.fixture()
def faker() -> Faker:
    return Faker(locale='ru_RU')


@pytest.fixture(scope='function')
def container() -> Container:
    return init_dummy_container()


@pytest.fixture()
def http_client(container: Container) -> BaseHTTPClient:
    return container.resolve(BaseHTTPClient)


@pytest.fixture()
def ai_client(container: Container) -> BaseAIClient:
    return container.resolve(BaseAIClient)


@pytest.fixture()
def user_service(container: Container) -> BaseUserService:
    return container.resolve(BaseUserService)


@pytest.fixture()
def chat_service(container: Container) -> BaseChatService:
    return container.resolve(BaseChatService)


@pytest.fixture()
def message_service(container: Container) -> BaseMessageService:
    return container.resolve(BaseMessageService)


@pytest.fixture
def vk_service(container: Container) -> BaseVKService:
    return container.resolve(BaseVKService)


@pytest.fixture()
def url(faker: Faker) -> str:
    return faker.uri()
