from info import filters
from botii import Bot,Bot1
@Bot1.on_message(filters.command('start') & filters.private)
async def start_mhsg_admins(client, message):
    await message.reply_text('hi')
@Bot.on_message(filters.command('start') & filters.private)
async def start_msg_admins(client, message):
    await message.reply_text('hi')
