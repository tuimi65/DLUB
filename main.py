from config import Bot
from pyrogram import Client

plugins = dict(root="plugins")

if __name__ == "__main__":
    Client("dlub", api_id=Bot.API_ID, api_hash=Bot.API_HASH, session_string=Bot.SESSION_STRING, plugins=plugins, in_memory=True).run()
    