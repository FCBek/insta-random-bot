import logging
import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

# Config
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Logger
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Languages
LANGUAGES = {
    "uz": "O'zbekcha",
    "ru": "Русский",
    "en": "English"
}

user_languages = {}

# Keyboards
def language_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for code, name in LANGUAGES.items():
        kb.add(KeyboardButton(name))
    return kb

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    user_languages[message.from_user.id] = "uz"
    await message.reply("Tilni tanlang / Выберите язык / Choose language:", reply_markup=language_keyboard())

@dp.message_handler(lambda msg: msg.text in LANGUAGES.values())
async def set_language(message: types.Message):
    for code, name in LANGUAGES.items():
        if message.text == name:
            user_languages[message.from_user.id] = code
            await message.reply(get_text("send_link", code))

@dp.message_handler(lambda msg: "instagram.com" in msg.text)
async def handle_instagram_link(message: types.Message):
    lang = user_languages.get(message.from_user.id, "en")
    # Simulyatsiya qilingan follower soni va random tanlash
    import random
    followers = ["user1", "user2", "user3", "user4", "user5"]
    count = len(followers)
    chosen = random.choice(followers)
    await message.reply(get_text("follower_count", lang).format(count))
    await message.reply(get_text("random_follower", lang).format(chosen))

def get_text(key, lang):
    texts = {
        "send_link": {
            "uz": "Instagram profil havolasini yuboring.",
            "ru": "Отправьте ссылку на Instagram профиль.",
            "en": "Send the Instagram profile link."
        },
        "follower_count": {
            "uz": "Obunachilar soni: {} ta",
            "ru": "Количество подписчиков: {}",
            "en": "Follower count: {}"
        },
        "random_follower": {
            "uz": "Tasodifiy tanlangan obunachi: {}",
            "ru": "Случайный подписчик: {}",
            "en": "Random follower: {}"
        }
    }
    return texts[key][lang]

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
