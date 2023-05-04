from info import filters
from pyrogram  import Client
@Client.on_message(filters.command('start') & filters.private)
async def start_msg_admins(client, message)
    await message.reply_text('hi')
