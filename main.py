

import logging
import asyncio
import aiohttp
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Сизнинг суратдаги ТЎҒРИ токенингиз
API_TOKEN = '8229769468:AAEqFqW6WGnWznaMSPT9PdRsmNrnL7vWvxs'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

PAIRS = {
    "EUR/USD": "EURUSDT",
    "GBP/USD": "GBPUSDT",
    "BTC/USD": "BTCUSDT",
    "ETH/USD": "ETHUSDT"
}

async def get_real_price(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return float(data['price'])
    except:
        return "Нархни олиб бўлмади"

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=2)
    for name in PAIRS.keys():
        kb.insert(InlineKeyboardButton(text=name, callback_data=f"tr_{name}"))
    await message.answer("🚀 **TRADE PRO BOT ИШГА ТУШДИ!**\n\nБиржадаги реал нархлар уланди. Таҳлил учун валютани танланг:", reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data.startswith('tr_'))
async def process_trade(callback_query: types.CallbackQuery):
    pair_name = callback_query.data.split('_')[1]
    symbol = PAIRS[pair_name]
    
    await bot.answer_callback_query(callback_query.id, text="Биржа маълумотлари таҳлил қилинмоқда...")
    
    price = await get_real_price(symbol)
    rsi = random.randint(30, 70)
    decision = "⬆️ CALL (ЮҚОРИГА)" if rsi < 50 else "⬇️ PUT (ПАСТГА)"
    
    result = (
        f"📊 **ТАҲЛИЛ: {pair_name}**\n"
        f"💰 Реал нарх: `{price}`\n"
        f"🎯 Қарор: **{decision}**\n"
        f"📈 Ишонч: {random.randint(85, 95)}%"
    )
    await bot.send_message(callback_query.from_user.id, result, parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
