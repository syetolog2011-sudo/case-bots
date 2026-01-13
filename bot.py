import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8383475541:AAEIGuu-Cs-Cf7nim40BxFgo8hvBl-0MQ_g"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🎰 Добро пожаловать в кейсы!\n\n"
        "Здесь ты можешь открывать кейсы и выигрывать ⭐"
    )

async def main():
    print("Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
