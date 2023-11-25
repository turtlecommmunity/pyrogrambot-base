import os
import logging
import pyrogram
from pyrogram import Client
from dotenv import load_dotenv
load_dotenv("config.env")

#Importing From Configs

APP_ID = int(os.environ.get("APP_ID", 6))
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

#Logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#Defining The Plugins Directory
plugins = dict(
    root="Turtlecommunity/plugins",
)

#Finally Defining And Running The Client Turtle
print("Successfully deployed!")
print("Base For This Bot Belongs To --> https://github.com/turtlecommmunity/pyrogram-base")
Client(
    "yDixx",
    bot_token=BOT_TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    workers=24,
    in_memory=True,
    plugins=plugins
).run()
