from info import filters
from botii import Bot,Bot1
@Bot.on_message(filters.command('start') & filters.private)
@Bot.on_message(filters.command('start') & filters.private)
async def start_msg_admins(client, message):
    mk=await message.reply_text('hi')
    await message.reply_text(f'{mk.id}hi')
