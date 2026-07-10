from src.domain.entities.users import User


def convert_user_to_dict(user: User) -> dict:
    return {
        'vk_id': user.vk_id,
        'email': user.email,
        'name': user.name,
        'thread_id': user.thread_id,
    }


def convert_user_from_dict(user: dict) -> User:
    return User(
        vk_id=user.get('vk_id'),
        email=user.get('email'),
        name=user.get('name'),
        thread_id=user.get('thread_id'),
    )
