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
            plugins={"root": "plugins"},
            sleep_threshold=4,
        )

    async def start(self):
        await super().start()
        await Media.ensure_indexes()
        
    async def stop(self, *args):
        await super().stop()
        

class Bot1(Client):
    
    def __init__(self):
        super().__init__(
            name='Mediasiearch',
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token='6332194321:AAE2pkCDZzeYkNfM_jd5gFt3wc-QyD6QfDY',
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        await Media.ensure_indexes()
        
    async def stop(self, *args):
        await super().stop() 
async def main():
    app=[Bot(),Bot1()]
    await compose(app)
