class ErrorTextProvider:
    @staticmethod
    def no_chat_access() -> str:
        return 'Нет доступа.'

    @staticmethod
    def connection_error() -> str:
        return 'Произошла ошибка соединения. Повторите свой вопрос, пожалуйста.'


class TextProvider:
    def __init__(self) -> None:
        self.errors: ErrorTextProvider = ErrorTextProvider()


text_provider = TextProvider()
