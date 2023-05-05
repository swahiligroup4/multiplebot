from info import filters
from botii import Bot,Bot1
@App.on_message(filters.command('start') & filters.private)
async def start_msg_admins(client, message):
    await message.reply_text('hi')
