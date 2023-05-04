from info import filters
from botii import Bot  
Bot.BOT_TOKEN='6289396925:AAGBWFC0s_VuE27HFNFHPRwg2HVTmQGsJL0'
@Bot.on_message(filters.command('start') & filters.private)
async def start_msg_admins(client, message):
    await message.reply_text('hi')
