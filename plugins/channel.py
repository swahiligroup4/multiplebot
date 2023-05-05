from info import filters
from pyrogram.handlers import MessageHandler
from botii import Bot,Bot1

def start_msg_admins(client, message):
    print('hi')
Bot1.add_handler(MessageHandler(start_msg_admins),filters.command("test"))
Bot.add_handler(MessageHandler(start_msg_admins),filters.command("test"))
