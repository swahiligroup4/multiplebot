from info import filters
from bot import app
app=app(bot_token='2136703772:AAH7YT8ngkmRmsSgU8BUX1zjQT8hw8JVdyE')
@app.on_message(filters.command('start') & filters.private)
async def start_msg_admins(client, message):
    await message.reply_text('hi')
