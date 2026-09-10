import logging

from aiogram import Bot,Dispatcher


from dotenv import load_dotenv
import os

load_dotenv()

dp = Dispatcher()

async def main():
        if token := os.getenv("BOT_TOKEN"):
            bot = Bot(token=token)
            try:
                await dp.start_polling(bot)
                logging.info("Bot started")
            finally:
                await bot.close()
        else:
            raise ValueError("Bot token not provided")
