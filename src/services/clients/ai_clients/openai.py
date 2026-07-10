import asyncio
from collections import defaultdict
from dataclasses import (
    dataclass,
    field,
)

from openai import (
    AsyncOpenAI,
    BadRequestError,
)

from src.domain.entities.users import User
from src.services.clients.ai_clients.base import BaseAIClient
from src.services.exceptions.ai_clients import AIBadRequestException


@dataclass
class OpenAIClient(BaseAIClient):
    client: AsyncOpenAI
    assistant_id: str
    locks: dict = field(
        default_factory=lambda: defaultdict(asyncio.Lock),
        kw_only=True,
    )

    async def _create_thread_id(self) -> str:
        thread = await self.client.beta.threads.create()
        return thread.id

    async def generate_response(self, request: str, user: User) -> str:
        try:
            if user.thread_id is None:
                user.set_thread_id(await self._create_thread_id())
            lock = self.locks[user.thread_id]

            async with lock:
                await self.client.beta.threads.messages.create(
                    thread_id=user.thread_id,
                    role='user',
                    content=request,
                )
                run = await self.client.beta.threads.runs.create(
                    thread_id=user.thread_id,
                    assistant_id=self.assistant_id,
                )

                while run.status in ('queued', 'in_progress'):
                    await asyncio.sleep(1)
                    run = await self.client.beta.threads.runs.retrieve(
                        thread_id=user.thread_id,
                        run_id=run.id,
                    )

                messages = await self.client.beta.threads.messages.list(thread_id=user.thread_id)
                response = messages.data[0].content[0].text.value

                return self._strip_markdown(text=response)

        except BadRequestError as error:
            raise AIBadRequestException(error=error.args[0])
