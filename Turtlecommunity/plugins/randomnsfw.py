from pyrogram import Client, filters
from pyrogram.types import Message
from io import BytesIO
import requests

@Client.on_message(filters.command(["ass"], prefixes=["?", "/"]))
async def ass(c: Client, m: Message):
    api_url = 'https://mdzapi.mdzhost.cloud/nsfw/ass?apitoken=zeus7676'
    response = requests.get(api_url)

    if response.status_code == 200:
        photo_stream = BytesIO(response.content)
        photo_stream.name = "image.jpg"
        await m.reply_photo(photo=photo_stream, caption='Ass')
        os.remove(photo_stream)
    else:
        await m.reply_text('erro')

@Client.on_message(filters.command(["cum"], prefixes=["?", "/"]))
async def cum(c: Client, m: Message):
    api_url = 'https://mdzapi.mdzhost.cloud/nsfw/cum?apitoken=zeus7676'
    response = requests.get(api_url)

    if response.status_code == 200:
        photo_stream = BytesIO(response.content)
        photo_stream.name = "image.jpg"
        await m.reply_photo(photo=photo_stream, caption='Cum')
        os.remove(photo_stream)
    else:
        await m.reply_text('erro')

@Client.on_message(filters.command(["ero"], prefixes=["?", "/"]))
async def ero(c: Client, m: Message):
    api_url = 'https://mdzapi.mdzhost.cloud/nsfw/ero?apitoken=zeus7676'
    response = requests.get(api_url)

    if response.status_code == 200:
        photo_stream = BytesIO(response.content)
        photo_stream.name = "image.jpg"
        await m.reply_photo(photo=photo_stream, caption='Ero')
        os.remove(photo_stream)
    else:
        await m.reply_text('erro')

@Client.on_message(filters.command(["hentai"], prefixes=["?", "/"]))
async def hentai(c: Client, m: Message):
    api_url = 'https://mdzapi.mdzhost.cloud/nsfw/hentai?apitoken=zeus7676'
    response = requests.get(api_url)

    if response.status_code == 200:
        photo_stream = BytesIO(response.content)
        photo_stream.name = "image.jpg"
        await m.reply_photo(photo=photo_stream, caption='Hentai')
        os.remove(photo_stream)
    else:
        await m.reply_text('erro')

@Client.on_message(filters.command(["pussy"], prefixes=["?", "/"]))
async def hentai(c: Client, m: Message):
    api_url = 'https://mdzapi.mdzhost.cloud/nsfw/pussy?apitoken=zeus7676'
    response = requests.get(api_url)

    if response.status_code == 200:
        photo_stream = BytesIO(response.content)
        photo_stream.name = "image.jpg"
        await m.reply_photo(photo=photo_stream, caption='teste')
        os.remove(photo_stream)
    else:
        await m.reply_text('erro')


