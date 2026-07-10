import pytest
from faker import Faker

from src.domain.entities.users import User
from src.services.clients.ai_clients.base import BaseAIClient
from src.services.exceptions.ai_clients import AIBadRequestException
from src.tests.factories.users import UserFactory


@pytest.mark.asyncio
async def test_ai_client_generate_response_success(
    ai_client: BaseAIClient,
    faker: Faker,
):
    user: User = UserFactory()

    response: str = faker.text()
    ai_client._set_response(response)

    result: str = await ai_client.generate_response(
        request=faker.text(),
        user=user,
    )

    assert result == response, f'{result=}'


@pytest.mark.asyncio
async def test_ai_client_generate_response_bad_request(
    ai_client: BaseAIClient,
    faker: Faker,
):
    user: User = UserFactory()
    with pytest.raises(AIBadRequestException):
        await ai_client.generate_response(
            request=faker.text(),
            user=user,
        )
