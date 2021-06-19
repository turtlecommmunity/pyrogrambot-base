from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["start"]))
async def start(_, message):
    text= "Hey!! Thanks For Using This As Base For Your Bot\nVisit @turtlecommunitytg For Any Help"
    await message.reply_photo(
        caption=text,
        photo="https://telegra.ph/file/5a2e0f3c4e3268737c6b3.jpg")