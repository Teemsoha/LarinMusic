import random
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union
from Auput import app

@app.on_message(filters.command("طرح"))
async def Saidi(_, message: Message):
    JABWA = "بلح"
    await message.reply_text(AHMAD)
