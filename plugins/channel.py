from info import filters 
from botii import Bot,Bot1
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
@Bot.on_message(filters.command('start') & filters.private)
@Bot1.on_message(filters.command('start') & filters.private)
async def start_msg_admins(client, message):
    mk=await message.reply_text('hi')
    await message.reply_text(f'{mk.id}hi',reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('yes',callbackquery ='ccc')]]))
@Bot1.on_callback_query()
async def about_ucbq(client, query):
    if query.data=='ccc':
        return 'yes'
