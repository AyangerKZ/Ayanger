import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = '7248047649:AAGhFeM1xYcgM4vBFS1hB2eMZW8ztD7BNDU'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message):
    # Создаем кнопку
    button = types.KeyboardButton(text="Открыть веб страницу", web_app=WebAppInfo(url="https://ayangerkz.github.io/Ayanger/"))
    # Создаем разметку и добавляем кнопку
    markup = types.ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)
    await message.answer("Привет, Мой друг", reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



