import asyncio

import pytest
from faker import Faker

from src.domain.entities.users import User
from src.services.clients.ai_clients.n8n import N8NClient
from src.tests.factories.users import UserFactory


@pytest.mark.asyncio
async def test_n8n_client_generate_response_success(n8n_client: N8NClient):
    user: User = UserFactory()
    request = 'Как твои дела? Как тебя зовут?'

    response: str = await n8n_client.generate_response(
        request=request,
        user=user,
    )
    assert isinstance(response, str), f'{response}='


@pytest.mark.asyncio
async def test_n8n_client_generate_response_3_requests_different_users(n8n_client: N8NClient):
    users: list[User] = UserFactory.build_batch(3)
    request = 'Как твои дела? Как тебя зовут?'
    tasks = [
        asyncio.create_task(
            n8n_client.generate_response(
                request=request,
                user=user,
            ),
        )
        for user in users
    ]
    result, _ = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

    assert len(result) == 3, f'{result=}'


@pytest.mark.asyncio
async def test_n8n_client_generate_response_3_requests_one_user(
    n8n_client: N8NClient,
    faker: Faker,
):
    user: User = UserFactory()
    requests = [
        faker.text(max_nb_chars=140)
        for _ in range(3)
    ]
    tasks = [
        asyncio.create_task(
            n8n_client.generate_response(
                request=request,
                user=user,
            ),
        )
        for request in requests
    ]
    result, _ = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

    assert len(result) == 3, f'{result=}'
