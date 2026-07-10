import pytest
from httpx import AsyncClient

from src.project.configs import settings
from src.services.clients.ai_clients.n8n import N8NClient


@pytest.fixture()
def n8n_client() -> N8NClient:
    return N8NClient(
        url=settings.N8N_URL,
        client=AsyncClient(),
    )
