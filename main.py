from os import getenv
from dotenv import load_dotenv
import asyncio
import logging
from app.utils.logger_config import setup_logger

from aiogram import Bot, Dispatcher

from app.handlers.start import router as start_router
from app.handlers.help import router as help_router
from app.handlers.tasks import router as list_router


load_dotenv()
TOKEN = getenv("BOT_TOKEN") or ""

setup_logger()
logger = logging.getLogger(__name__)

dp = Dispatcher()
dp.include_routers(start_router, help_router, list_router)

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.debug("Сообщение типа INFO")
    asyncio.run(main())