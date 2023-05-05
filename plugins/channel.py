from info import filters
from pyrogram.handlers import MessageHandler
from botii import Bot,Bot1

async def start_msg_admins(client, message):
    await message.reply_text('hi')
Bot1.add_handler(MessageHandler(start_msg_admins),Filters.command("test"))
Bot.add_handler(MessageHandler(start_msg_admins),Filters.command("test"))
