from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("𝑺𝑯𝑨𝑹𝑬 𝒀𝑶𝑼𝑹 𝑳𝑰𝑵𝑲" ,url=f"https://t.me/share/url?url=https://t.me/movie_hub09_bot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"𝑹𝑬𝑭𝑬𝑹 𝑨𝑵𝑫 𝑾𝑰𝑵𝑵𝑬𝑹 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 𝑴𝑬𝑴𝑩𝑬𝑹𝑺𝑯𝑰𝑷 𝑳𝑰𝑵𝑲 : https://t.me/movie_hub09_bot?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    
