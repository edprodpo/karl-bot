from punq import (
    Container,
    Scope,
)

from src.project.containers import _init_container
from src.services.chats.base import BaseChatService
from src.services.chats.memory import MemoryChatService
from src.services.clients.ai_clients.base import BaseAIClient
from src.services.clients.ai_clients.memory import MemoryAIClient
from src.services.clients.http_clients.base import BaseHTTPClient
from src.services.clients.http_clients.memory import MemoryHTTPClient
from src.services.messages.base import BaseMessageService
from src.services.messages.memory import MemoryMessageService
from src.services.users.base import BaseUserService
from src.services.users.memory import MemoryUserService
from src.services.vk_service.base import BaseVKService
from src.services.vk_service.memory import MemoryVKService


def init_dummy_container() -> Container:
    container = _init_container()

    # clients
    container.register(
        service=BaseHTTPClient,
        instance=MemoryHTTPClient(),
        scope=Scope.singleton,
    )
    container.register(
        service=BaseAIClient,
        instance=MemoryAIClient(),
        scope=Scope.singleton,
    )

    # services
    container.register(
        service=BaseUserService,
        factory=MemoryUserService,
        scope=Scope.singleton,
    )
    container.register(
        service=BaseChatService,
        factory=MemoryChatService,
        scope=Scope.singleton,
    )
    container.register(
        service=BaseMessageService,
        factory=MemoryMessageService,
        scope=Scope.singleton,
    )
    container.register(
        service=BaseVKService,
        instance=MemoryVKService(),
        scope=Scope.singleton,
    )

    return container
