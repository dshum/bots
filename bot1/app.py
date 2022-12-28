import os, logging
from aiogram import Bot, Dispatcher, executor, types
from os.path import join, dirname
from dotenv import load_dotenv

# Initialize env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_TOKEN = os.environ.get("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.lower() == "what is your name?":
        await message.answer("I am Bot")
    elif message.text.lower() == "who is your owner?":
        await message.answer("Shumeev")
    else:
        await message.answer(message.as_json())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
