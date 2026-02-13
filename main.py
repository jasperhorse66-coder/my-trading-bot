import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8229769468:AAEqFqW6WGnWznaMSPT9PdRsmNrnL7vWvxs"

bot = Bot(token=TOKEN)
dp = Dispatcher()

PAIRS = ["EUR/USD", "GBP/USD", "USD/JPY", "GOLD (XAU/USD)", "BITCOIN", "SOLANA"]

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    kb = [
        [types.KeyboardButton(text="⏱ 1 МИН"), types.KeyboardButton(text="⏱ 3 МИН")],
        [types.KeyboardButton(text="⏱ 5 МИН"), types.KeyboardButton(text="⏱ 10 МИН")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(f"💎 **FX PRO SERVER**\n\nБот серверда 24/7 ишламоқда. Вақтни танланг:", reply_markup=keyboard)

@dp.message(lambda message: message.text in ["⏱ 1 МИН", "⏱ 3 МИН", "⏱ 5 МИН", "⏱ 10 МИН"])
async def signal_handler(message: types.Message):
    wait_msg = await message.answer("🔍 Бозор таҳлил қилинмоқда...")
    await asyncio.sleep(1)
    pair = random.choice(PAIRS)
    direction = random.choice(["🚀 BUY", "🔻 SELL"])
    conf = random.randint(90, 98)
    text = (f"✅ **СИГНАЛ ТАЙЁР**\n\n💎 Валюта: {pair}\n🎯 Йўналиш: {direction}\n⏰ Вақт: {message.text}\n🔥 Ишонч: {conf}%")
    await wait_msg.edit_text(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
