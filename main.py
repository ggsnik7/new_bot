import asyncio
import logging

from aiogram import Bot, Dispatcher
from config.cfg import Config, load_config
from handlers import other, user
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.user import inline_button_router
from handlers.middlewares import UpdateMiddleware

# Функция конфигурирования и запуска бота
async def main():

    # Загружаем конфиг в переменную config
    config: Config = load_config()
    
    # Задаём базовую конфигурацию логирования
    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format,
    )
    # Инициализируем бот и диспетчер
    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
    dp = Dispatcher()
    #Регистрируем мидлвари в диспетчере
    dp.update.middleware(UpdateMiddleware())

    # Регистриуем роутеры в диспетчере
    dp.include_router(user.inline_button_router)
    dp.include_router(other.other_router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())






