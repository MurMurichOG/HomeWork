import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from aiogram.filters import Command
import logging
import random

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN1'))
dp = Dispatcher()

@dp.message(Command("start"))
async def greet(message: types.Message):
    await message.answer(f"Здравствуй, {message.from_user.full_name}!")

@dp.message(Command("myinfo"))
async def info(message: types.Message):
    await message.answer(f"Ваш id: {message.from_user.id}, Ваше имя: {message.from_user.first_name}, Ваш никнейм: {message.from_user.username}")

@dp.message(Command("pic"))
async def send_pic(message: types.Message):
    files = [
        "images/Без названия (2).jfif",
        "images/1200px-RedCat_8727.jpg",
        "images/getty_creative.jpeg.webp",
        "images/large-cat-breed-1553197454.jpg",
        "images/Без названия.jfif"
    ]
    random_element = types.FSInputFile(random.choice(files))
    await message.answer_photo(photo=random_element, caption="Кот")

async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Приветствие"),
        types.BotCommand(command="pic", description="Получить рандомную картинку"),
        types.BotCommand(command="myinfo", description="Моя информация")
    ])
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())