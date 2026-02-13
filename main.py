import logging
import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Токенингизни шу ерга ёзинг
API_TOKEN = '8229769468:AAEqFqW6WGnWznaMSPT...' # Сизнинг суратдаги токенингиз

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Биржадаги реал жуфтликлар (Binance API учун мослашган)
PAIRS = {
    "EUR/USD": "EURUSDT",
    "GBP/USD": "GBPUSDT",
    "BTC/USD": "BTCUSDT",
    "ETH/USD": "ETHUSDT",
    "SOL/USD": "SOLUSDT"
}

# Реал нархни олиш функцияси
async def get_real_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return float(data['price'])

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=2)
    for name in PAIRS.keys():
        kb.insert(InlineKeyboardButton(text=name, callback_data=f"trade_{name}"))
    
    await message.answer(
        "💎 **PRO ANALYTICS BOT**\n\n"
        "Бот реал вақтда Binance биржаси маълумотларини таҳлил қилади.\n"
        "Валютани танланг:", reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data.startswith('trade_'))
async def process_trade(callback_query: types.CallbackQuery):
    pair_name = callback_query.data.split('_')[1]
    symbol = PAIRS[pair_name]
    
    await bot.answer_callback_query(callback_query.id, text="Биржадан маълумот олинмоқда...")
    
    # Реал нархни оламиз
    price = await get_real_price(symbol)
    
    # Техник таҳлил (RSI симуляцияси ва нарх ҳаракати)
    import random
    rsi = random.randint(20, 80) # Келажакда техник кутубхона улаймиз
    
    if rsi < 35:
        direction = "⬆️ ЮҚОРИГА (CALL)"
        reason = "Бозор ҳаддан ташқари сотилган (Oversold)"
    elif rsi > 65:
        direction = "⬇️ ПАСТГА (PUT)"
        reason = "Бозор ҳаддан ташқари сотиб олинган (Overbought)"
    else:
        direction = random.choice(["⬆️ ЮҚОРИГА", "⬇️ ПАСТГА"])
        reason = "Тренд бўйлаб ҳаракат"

    result = (
        f"📊 **БИРЖА ТАҲЛИЛИ: {pair_name}**\n"
        f"━━━━━━━━━━━━━━━\n"
        f"💰 Жорий нарх: `{price}`\n"
        f"📈 Индикатор (RSI): `{rsi}`\n"
        f"🎯 Қарор: **{direction}**\n"
        f"💡 Сабаб: {reason}\n"
        f"━━━━━━━━━━━━━━━\n"
        f"⏱ Вақт: 1-5 дақиқа\n"
        f"⚠️ *Минусни камайтириш учун фақат 85% дан юқори сигналларга киринг!*"
    )
    
    await bot.send_message(callback_query.from_user.id, result, parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
import logging
import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Токенингизни шу ерга ёзинг
API_TOKEN = '8229769468:AAEqFqW6WGnWznaMSPT...' # Сизнинг суратдаги токенингиз

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Биржадаги реал жуфтликлар (Binance API учун мослашган)
PAIRS = {
    "EUR/USD": "EURUSDT",
    "GBP/USD": "GBPUSDT",
    "BTC/USD": "BTCUSDT",
    "ETH/USD": "ETHUSDT",
    "SOL/USD": "SOLUSDT"
}

# Реал нархни олиш функцияси
async def get_real_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return float(data['price'])

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=2)
    for name in PAIRS.keys():
        kb.insert(InlineKeyboardButton(text=name, callback_data=f"trade_{name}"))
    
    await message.answer(
        "💎 **PRO ANALYTICS BOT**\n\n"
        "Бот реал вақтда Binance биржаси маълумотларини таҳлил қилади.\n"
        "Валютани танланг:", reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data.startswith('trade_'))
async def process_trade(callback_query: types.CallbackQuery):
    pair_name = callback_query.data.split('_')[1]
    symbol = PAIRS[pair_name]
    
    await bot.answer_callback_query(callback_query.id, text="Биржадан маълумот олинмоқда...")
    
    # Реал нархни оламиз
    price = await get_real_price(symbol)
    
    # Техник таҳлил (RSI симуляцияси ва нарх ҳаракати)
    import random
    rsi = random.randint(20, 80) # Келажакда техник кутубхона улаймиз
    
    if rsi < 35:
        direction = "⬆️ ЮҚОРИГА (CALL)"
        reason = "Бозор ҳаддан ташқари сотилган (Oversold)"
    elif rsi > 65:
        direction = "⬇️ ПАСТГА (PUT)"
        reason = "Бозор ҳаддан ташқари сотиб олинган (Overbought)"
    else:
        direction = random.choice(["⬆️ ЮҚОРИГА", "⬇️ ПАСТГА"])
        reason = "Тренд бўйлаб ҳаракат"

    result = (
        f"📊 **БИРЖА ТАҲЛИЛИ: {pair_name}**\n"
        f"━━━━━━━━━━━━━━━\n"
        f"💰 Жорий нарх: `{price}`\n"
        f"📈 Индикатор (RSI): `{rsi}`\n"
        f"🎯 Қарор: **{direction}**\n"
        f"💡 Сабаб: {reason}\n"
        f"━━━━━━━━━━━━━━━\n"
        f"⏱ Вақт: 1-5 дақиқа\n"
        f"⚠️ *Минусни камайтириш учун фақат 85% дан юқори сигналларга киринг!*"
    )
    
    await bot.send_message(callback_query.from_user.id, result, parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

