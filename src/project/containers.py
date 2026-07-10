from functools import lru_cache

from vkbottle import API

import httpx
from openai import AsyncOpenAI
from punq import (
    Container,
    Scope,
)

from src.project.configs import settings
from src.services.chats.admin import AdminAPIChatService
from src.services.chats.base import BaseChatService
from src.services.clients.ai_clients.base import BaseAIClient
from src.services.clients.ai_clients.n8n import N8NClient
from src.services.clients.ai_clients.openai import OpenAIClient
from src.services.clients.http_clients.base import BaseHTTPClient
from src.services.clients.http_clients.httpx_client import HTTPXClient
from src.services.messages.admin import AdminAPIMessageService
from src.services.messages.base import BaseMessageService
from src.services.use_cases.ai.generate_response import GenerateGroupChatResponseUseCase
from src.services.use_cases.users.get_or_create import GetOrCreateUserUseCase
from src.services.users.admin import AdminAPIUserService
from src.services.users.base import BaseUserService
from src.services.vk_service.base import BaseVKService
from src.services.vk_service.vk import VKService


@lru_cache(1)
def get_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(
        service=API,
        instance=API(settings.VK_API_KEY),
        scope=Scope.singleton,
    )

    # builders
    def _build_httpx_client() -> HTTPXClient:
        return HTTPXClient(client=httpx.AsyncClient())

    def _build_openai_client() -> OpenAIClient: # noqa
        return OpenAIClient(
            client=AsyncOpenAI(
                api_key=settings.OPENAI_API_KEY,
                http_client=httpx.AsyncClient(
                    proxy=settings.GENERAL_PROXY,
                    transport=httpx.AsyncHTTPTransport(local_address="0.0.0.0"),
                ),
                max_retries=3,
            ),
            assistant_id=settings.OPENAI_ASSISTANT_ID,
        )

    def _build_n8n_client() -> N8NClient:
        return N8NClient(
            client=httpx.AsyncClient(),
            url=settings.N8N_URL,
        )

    # clients
    container.register(
        service=BaseHTTPClient,
        factory=_build_httpx_client,
        scope=Scope.singleton,
    )
    container.register(
        service=BaseAIClient,
        factory=_build_n8n_client,
        scope=Scope.singleton,
    )

    # services
    container.register(
        service=BaseUserService,
        factory=AdminAPIUserService,
        scope=Scope.singleton,
    )
    container.register(
        service=BaseChatService,
        factory=AdminAPIChatService,
        scope=Scope.singleton,
    )
    container.register(
        service=BaseMessageService,
        factory=AdminAPIMessageService,
        scope=Scope.singleton,
    )
    container.register(
        service=BaseVKService,
        factory=VKService,
        scope=Scope.singleton,
    )

    # use cases
    container.register(GetOrCreateUserUseCase)
    container.register(GenerateGroupChatResponseUseCase)

    return container
