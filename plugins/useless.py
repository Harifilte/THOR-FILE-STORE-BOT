from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from helper_func import get_readable_time


@Bot.on_message(filters.command("stats") & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private)
async def useless(_, message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
