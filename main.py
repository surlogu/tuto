from pyrogram import Client, filters
import os, shutil
from creds import my
import logging

logging.basicConfig(level=logging.INFO)


TuTo = Client(
    "TuTo bot",
    bot_token = my.BOT_TOKEN,
    api_id = my.API_ID,
    api_hash = my.API_HASH
)


@TuTo.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(f"Hello {message.from_user.first_name},\nI'm TuTo", True)
@TuTo.on_message(filters.command("help"))
async def start(client, message):
    await message.reply_text("Help Message", True)
    
TuTo.run()
