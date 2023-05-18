from info import filters 

from botii import Bot,Bot1
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
@Bot.on_message(filters.command('start') & filters.private)
@Bot1.on_message(filters.command('test') & filters.private)
async def start_msg_admins(client, message):
    mk=await message.reply_text('hi')
    mk2=await message.reply_text(f'{mk.id}hi',reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('yes', callback_data ='ccc')]]))
@Bot1.on_callback_query()
async def about_ucbq(client, query):
    if query.data=='ccc':
        return 'yes'
