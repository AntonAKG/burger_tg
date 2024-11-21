import asyncio
import logging
from aiogram import Bot, Dispatcher

from app.handlers.cmd_base import router as start_router
from app.settings import settings


async def main():
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher()
    bot = Bot(token=settings.token.get_secret_value())

    dp.include_routers(
        start_router
    )

    await dp.run_polling(bot)


if __name__ == "__main__":
    try:
        import nest_asyncio

        nest_asyncio.apply()
        asyncio.run(main())
    except RuntimeError as e:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
