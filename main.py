import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
TWITCH_URL = os.getenv("TWITCH_URL")
TIKTOK_URL = os.getenv("TIKTOK_URL")
YOUTUBE_URL = os.getenv("YOUTUBE_URL")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(F.is_automatic_forward == True)
async def on_forwarded_post(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📺 YouTube", url=YOUTUBE_URL),
                InlineKeyboardButton(text="🎵 TikTok", url=TIKTOK_URL),
            ],
            [InlineKeyboardButton(text="🎮 Twitch", url=TWITCH_URL)]
        ]
    )

    gif_url = (
        "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDlnNDI1Z2p0c2FuYW45bjVnbm9qaWViNG5jZWRzdTB5"
        "cXlvYnZvayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IRFQYGCokErS0/giphy.gif"
    )


    caption=""

    await bot.send_animation(
        chat_id=message.chat.id,
        animation=gif_url,
        caption=caption,
        reply_to_message_id=message.message_id,
        reply_markup=keyboard )

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
