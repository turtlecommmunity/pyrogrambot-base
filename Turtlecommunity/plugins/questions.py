from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ChatType

from functools import wraps
import random
import json

AWSWER_FILE = "Turtlecommunity/utils/database/info.json"
GROUPS_DB = "Turtlecommunity/utils/database/groups.json"
DONO = "5498248090"

def apnsdono(func):
    @wraps(func)
    async def wrapped(c: Client, m: Message, *args, **kwargs):
        if str(m.from_user.id) == DONO:
            return await func(c, m, *args, **kwargs)
        else:
            await m.reply("❌ <b>Acesso Restrito</b> ❌\n\n👮🏼‍♀️ <i>Apenas devs do bot tem acesso a este comando.</i>")
    return wrapped

def load_acertos():
    try:
        with open(AWSWER_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_acertos(acertos):
    with open(AWSWER_FILE, 'w') as file:
        json.dump(acertos, file)

def load_grupos():
    try:
        with open(GROUPS_DB, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_grupo(user_id, chat_id, chat_title):
    grupos = load_grupos()
    grupos[str(chat_id)] = {'user_id': user_id, 'chat_title': chat_title}
    with open(GROUPS_DB, 'w') as file:
        json.dump(grupos, file) 

@Client.on_message(filters.command(["quiz"], prefixes=["?", "/"]))
async def quiz(c: Client, m: Message):
    if m.chat.type != ChatType.PRIVATE:
        chat_data = c.get_chat_data(m.chat.id)
        if not chat_data.get('quiz_in_progress', False):
            with open('quiz.json', 'r', encoding='utf-8') as file:
                questions = json.load(file)

            question = random.choice(questions)
            chat_data['current_question'] = {'resposta_correta': question['resposta']}
            chat_data['quiz_in_progress'] = True

            await m.reply(f"\n✏️ *Pergunta:* `{question['pergunta']}`\n")
        else:
            await m.reply_text("Já tem um quiz em andamento.")
    else:
        await m.reply_text("Só em grupos.")

async def ask_another_question(c: Client, m: Message) -> None:
    chat_data = c.get_chat_data(m.chat.id)
    if chat_data.get('quiz_in_progress', False):
        with open('quiz.json', 'r', encoding='utf-8') as file:
            questions = json.load(file)

        question = random.choice(questions)
        chat_data['current_question'] = {'resposta_correta': question['resposta']}
        await m.reply_text(f"\n✏️ *Pergunta:* `{question['pergunta']}`\n")

async def check_answer(c: Client, m: Message) -> None:
    chat_data = c.get_chat_data(m.chat.id)
    if chat_data.get('quiz_in_progress', False):
        acertos = load_acertos()

        user_id = str(m.from_user.id)
        user_answer = m.text.lower()
        current_question = chat_data.get('current_question', {})
        correct_answer = current_question.get('resposta_correta', '').lower()

        if user_answer == correct_answer:
            username = m.from_user.username

            if user_id in acertos:
                acertos[user_id]['acertos'] += 1
            else:
                acertos[user_id] = {'username': username, 'id': user_id, 'acertos': 1}

            save_acertos(acertos)
            await m.reply_text(f"Parabéns @{username}\nAcertos: {acertos[user_id]['acertos']}")
            await ask_another_question(c, m)

@Client.on_message(filters.command(["rank"], prefixes=["?", "/"]))
async def placar(c: Client, m: Message):
    acertos = load_acertos()

    if not acertos:
        await m.reply_text("nenhum banco de dados foi encontrado")
        return

    ranksla = sorted(acertos.values(), key=lambda x: x['acertos'], reverse=True)[:5]

    message = "Top 5\n"
    for index, player in enumerate(ranksla, start=1):
        message += f"{index}  @{player['username']} - Acertos: {player['acertos']}\n"

    await m.reply_html(message)

@Client.on_message(filters.command(["resp"], prefixes=["?", "/"]))
@apnsdono
async def resp(c: Client, m: Message):
    if m.command:
        question_text = " ".join(m.command).lower()
        with open('quiz.json', 'r', encoding='utf-8') as file:
            questions = json.load(file)

        for question in questions:
            if question['pergunta'].lower() == question_text:
                await m.reply_text(f"resposta: {question['resposta']}")
                return

        await m.reply_text("a pergunta não existe no json")
    else:
        await m.reply_text("pergunta")

@Client.on_message(filters.command(["stats"], prefixes=["?", "/"]))
@apnsdono
async def usuarios(c: Client, m: Message):
    acertos = load_acertos()
    total_usuarios = len(acertos)
    mensagem = f"📊 *Estatísticas*\n🔎 *Usuários:* `{total_usuarios}`\n📁 *Grupos:* `0`"
    await m.reply_text(mensagem)
