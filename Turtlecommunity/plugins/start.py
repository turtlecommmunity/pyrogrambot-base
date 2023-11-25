import glob

from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


HELPABLE: list[str] = []

for modules in glob.glob("Turtlecommunity/plugins/*.py"):
    imported_module = import_module((modules)[:-3].replace("/", "."))
    if hasattr(imported_module, "__help__"):
        HELPABLE.append((modules.replace("/", ".")).split(".")[-2])


@Client.on_callback_query(filters.regex(pattern=r"^start_back$"))
@Client.on_message(filters.command("start"))
async def start(c: Client, m: Message | CallbackQuery):
    msg = ("<i>Olá <b>{}</b>!! Meu nome é <b>{}</b>. Estou aqui para divertir seu grupo</i>, <b>Fui feito com a biblioteca Pyrogram baseada na MTProto</b>").format(m.from_user.mention, c.me.first_name)
    button = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ℹ️ Sobre", callback_data="about"),
                InlineKeyboardButton(
                    text="📚 Comandos", callback_data="help_menu"),
            ],
        ]
    )
    if isinstance(m, Message):
        await m.reply(text=msg, reply_markup=button)
    else:
        await c.edit_message_text(
            chat_id=m.message.chat.id,
            message_id=m.message.id,
            text=msg,
            reply_markup=button,
        )

@Client.on_callback_query(filters.regex(pattern=r"about"))
async def about_menu(c: WhiterX, cb: CallbackQuery):
    keyboard = [
        [
            InlineKeyboardButton(await tld(cb.message.chat.id, "BACK_BNT"), "start_back"),
        ],
    ]
    text = ("<b>— yDixx</b>\n<b>Versão: <i>{}</i>").format("1.0.1")
    await cb.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), disable_web_page_preview=True)
