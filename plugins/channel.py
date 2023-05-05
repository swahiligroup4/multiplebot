from info import filters
from pyrogram.handlers import MessageHandler
from botii import Bot,Bot1
@Bot1.on_message(filters.command('start') & filters.private)
@Bot.on_message(filters.command('start') & filters.private)
async def start_msg_admins(client, message):
    await message.reply_text('hi')
Bot1.add_handler(MessageHandler(start_msg_admins))
Bot.add_handler(MessageHandler(start_msg_admins))
