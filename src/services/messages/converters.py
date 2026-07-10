from src.domain.entities.messages import Message


def convert_message_to_dict_w_vk_id(message: Message, vk_id: int) -> dict:
    return {
        'vk_id': vk_id,
        'request': message.request,
        'response': message.response,
    }
