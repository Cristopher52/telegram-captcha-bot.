import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

# === НАСТРОЙКИ ===
BOT_TOKEN = "8242487115:AAFwl9vOOHaU5_AiIL8g5BUs7i_zXUN7FDg"
CHANNEL_URL = "https://t.me/yourBags_there"

dp = Dispatcher()

# Кнопки капчи
def captcha_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="Я робот", callback_data="robot")
    kb.button(text="Я не робот", callback_data="not_robot")
    kb.adjust(2)
    return kb.as_markup()

# Кнопка перехода в канал
def channel_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="Перейти в канал", url=CHANNEL_URL)
    return kb.as_markup()

# /start
@dp.message(F.text.startswith("/start"))
async def start_handler(message: Message):
    await message.answer(
        "Вы не робот?\n\nНажмите кнопку ниже:",
        reply_markup=captcha_kb()
    )

# Если нажал "Я робот"
@dp.callback_query(F.data == "robot")
async def robot_clicked(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Хорошо 🙂")

# Если нажал "Я не робот"
@dp.callback_query(F.data == "not_robot")
async def not_robot_clicked(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        "Отлично! Нажмите кнопку ниже, чтобы перейти в канал:",
        reply_markup=channel_kb()
    )

# Запуск бота
async def main():
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
