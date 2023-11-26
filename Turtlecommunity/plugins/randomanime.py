from pyrogram import Client, filters
from pyrogram.types import Message
from io import BytesIO
import requests

@Client.on_message(filters.command(["loli"], prefixes=["?", "/"]))
async def loli(c: Client, m: Message):
    api_url = 'http://mdzapi.mdzhost.cloud/random/loli?apitoken=zeus7676'
    response = requests.get(api_url)

    if response.status_code == 200:
        photo_stream = BytesIO(response.content)
        photo_stream.name = "image.jpg"
        await m.reply_photo(photo=photo_stream, caption='teste')
    else:
        await m.reply_text('erro')

@Client.on_message(filters.command(["megumin"], prefixes=["?", "/"]))
async def megumin(c: Client, m: Message):
    api_url = 'http://mdzapi.mdzhost.cloud/random/megumin?apitoken=zeus7676'
    response = requests.get(api_url)

    if response.status_code == 200:
        photo_stream = BytesIO(response.content)
        photo_stream.name = "image.jpg"
        await m.reply_photo(photo=photo_stream, caption='teste')
    else:
        await m.reply_text('erro')
  
@Client.on_message(filters.command(["nezuko"], prefixes=["?", "/"]))
async def nezuko(c: Client, m: Message):
    api_url = 'http://mdzapi.mdzhost.cloud/random/nezuko?apitoken=zeus7676'
    response = requests.get(api_url)

    if response.status_code == 200:
        photo_stream = BytesIO(response.content)
        photo_stream.name = "image.jpg"
        await m.reply_photo(photo=photo_stream, caption='teste')
    else:
        await m.reply_text('erro')      

@Client.on_message(filters.command(["shina"], prefixes=["?", "/"]))
async def shina(c: Client, m: Message):
    api_url = 'http://mdzapi.mdzhost.cloud/random/shina?apitoken=zeus7676'
    response = requests.get(api_url)

    if response.status_code == 200:
        photo_stream = BytesIO(response.content)
        photo_stream.name = "image.jpg"
        await m.reply_photo(photo=photo_stream, caption='teste')
    else:
        await m.reply_text('erro')      
