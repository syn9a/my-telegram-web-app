from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram import F

API_TOKEN = '7792711359:AAFzAoW_1jTiznEMeIp2cajRPCz3dpaGC8I'  # Ваш токен от бота

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    print("Получена команда /start")  # Отладочное сообщение
    # Создаем клавиатуру с кнопкой
    keyboard = InlineKeyboardMarkup(inline_keyboard=[  # Здесь мы передаем список с кнопками
        [InlineKeyboardButton(
            text="Открыть мини-приложение",
            web_app={"url": "https://github.com/syn9a/my-telegram-web-app"}  # Замените на ваш URL
        )]
    ])

    await message.answer("Привет! Нажмите кнопку ниже, чтобы открыть мини-приложение.", reply_markup=keyboard)

if __name__ == "__main__":
    print("Запуск бота...")  # Отладочное сообщение
    dp.run_polling(bot)
