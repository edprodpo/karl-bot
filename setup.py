from src.application.bot import init_vk_bot
from src.project.configs import settings


if __name__ == '__main__':
    settings.config_logger()

    bot = init_vk_bot()
    bot.run_forever()
