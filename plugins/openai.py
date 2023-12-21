from info import OPENAI_API
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import OpenAI

ai_client = OpenAI(api_key=OPENAI_API)

@Client.on_message(filters.command("openai") & filters.private)
async def ask_question_pm(client, message):
    await ask_question(client, message)

@Client.on_message(filters.command("openai") & filters.group)
async def ask_question_group(client, message):
    if len(OPENAI_API) == 0:
        return await message.reply("OPENAI_API is empty")
    try:
        text = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("Command Incomplete!\nUsage: /openai your_question")
    msg = await message.reply("Searching...")
    try:
        response = ai_client.chat.completions.create(
            messages=[
                {"role": "user", "content": text}
            ],
            model="gpt-3.5-turbo"
        )
        await msg.edit(f"User: {message.from_user.mention}\nQuery: <code>{text}</code>\n\nResults:\n\n<code>{response.choices[0].message.content}</code>")
    except Exception as e:
        await msg.edit(f'Error - <code>{e}</code>')




