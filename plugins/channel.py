from info import filters
from botii import Bot  
Boti=Bot(bot_token='6289396925:AAGBWFC0s_VuE27HFNFHPRwg2HVTmQGsJL0')
@Boti.on_message(filters.command('start') & filters.private)
async def start_msg_admins(client, message):
    await message.reply_text('hi')
