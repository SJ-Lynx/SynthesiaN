from typing import Tuple
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# Configs
API_HASH = '5a6f3ad50a4cec3272b4b7dd6af0796f'
APP_ID = 7101379
BOT_TOKEN = '1971188577:AAHbMzj9uZz4Rw_CZF0s-ZxsapXMpsaj2DA'

START_BUTTONS=[
    [
        InlineKeyboardButton('Channel', url='https://t.me/SJa_bots'),
    ],
    [InlineKeyboardButton('Author', url='https://t.me/SJ_Lynx')],
]
sbot = Client('TikTokDL', api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@sbot.on_message(filters.command('start') & filters.private)
async def _start(bot, update):
  await update.reply_text(f"👋Welcome! I'm SynthesiaBot!\n\nThis bot is not working. When it works, we will let you know on our channel.", True, reply_markup=InlineKeyboardMarkup(START_BUTTONS))

sbot.run()
