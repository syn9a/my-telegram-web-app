rom aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "7792711359:AAFzAoW_1jTiznEMeIp2cajRPCz3dpaGC8I"  
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я работаю!")

if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
