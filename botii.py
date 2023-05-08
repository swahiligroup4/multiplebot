import logging
import logging.config
# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.ERROR)

from pyrogram import Client, __version__,compose
from pyrogram.raw.all import layer
from utils import Media
from info import SESSION, API_ID, API_HASH, BOT_TOKEN

class Bot(Client):
    
    def __init__(self):
        super().__init__(
            name=SESSION ,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugin"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        await Media.ensure_indexes()
        
    async def stop(self, *args):
        await super().stop()
        

class Bot1(Client):
    
    def __init__(self):
        super().__init__(
            name='Media siearch',
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token='2136703772:AAH7YT8ngkmRmsSgU8BUX1zjQT8hw8JVdyE',
            workers=50,
            plugins={"root": "plugin"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        await Media.ensure_indexes()
        
    async def stop(self, *args):
        await super().stop()
app=[Bot1(),Bot()]       
async def main():
    await compose(app)
