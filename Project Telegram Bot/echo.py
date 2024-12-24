
import  logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
logging.basicConfig(level=logging.INFO)


bot = Bot(token=TELEGRAM_BOT_TOKEN) 
Dp= Dispatcher(bot)

@Dp.message_handler(commands=['start','help'])
async def commmand_handler(message: types.Message):
    """
    This handler receives messages with '/start' or '/help' command
    """
    await message.reply("Hi\nI am Echo Bot!\nPowered by muskii.")




@Dp.message_handler()
async def echo(message: types.Message):
    """
    This will return echo
    """
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(Dp, skip_updates=True)