from src.domain.entities.chats import (
    Chat,
    TypeChat,
)


def convert_chat_to_dict(chat: Chat) -> dict:
    return {
        'chat_id': chat.chat_id,
        'title': chat.title,
        'type_chat': chat.type_chat.value,
        'is_active': chat.is_active,
    }


def convert_chat_from_dict(chat: dict) -> Chat:
    return Chat(
        chat_id=chat.get('chat_id'),
        title=chat.get('title'),
        type_chat=TypeChat(chat.get('type_chat')),
        is_active=chat.get('is_active'),
    )
