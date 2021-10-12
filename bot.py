from typing import Tuple
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# Configs
API_HASH = os.environ['API_HASH']
APP_ID = int(os.environ['APP_ID'])
BOT_TOKEN = os.environ['BOT_TOKEN']

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
