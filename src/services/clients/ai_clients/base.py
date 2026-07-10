import re
from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from src.domain.entities.users import User


@dataclass
class BaseAIClient(ABC):
    def _strip_markdown(self, text: str) -> str:
        # жирный и курсив (**text**, *text*, __text__, _text_)
        text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)
        text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)

        # inline code `code`
        text = re.sub(r'`([^`]*)`', r'\1', text)

        # блоки кода ```code```
        text = re.sub(r'```[\s\S]*?```', '', text)

        # заголовки ### text
        text = re.sub(r'^\s{0,3}#{1,6}\s*', '', text, flags=re.MULTILINE)

        # ссылки [текст](url) → текст
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)

        # изображения ![alt](url) → alt
        text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', text)

        # списки (-, *, +)
        text = re.sub(r'^\s*[-*+]\s+', '• ', text, flags=re.MULTILINE)

        # лишние пустые строки
        text = re.sub(r'\n{3,}', '\n\n', text)

        return text

    @abstractmethod
    async def generate_response(self, request: str, user: User) -> str:
        ...
