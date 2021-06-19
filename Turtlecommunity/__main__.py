import os
import logging
import pyrogram
from pyrogram import Client


#Importing From Configs

BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
API_HASH = os.environ.get("API_HASH", None)
APP_ID = int(os.environ.get("APP_ID", 6))


#Logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#Defining The Plugins Directory
plugins = dict(
    root="Turtlecommunity/plugins",
)

#Finally Defining And Running The Client Turtle
print("Successfully deployed!")
print("Turtle Rocks")
print("Base For This Bot Belongs To --> https://github.com/turtlecommmunity/pyrogram-base")
Client(
    "Turtle",
    bot_token=BOT_TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    plugins=plugins
).run()
