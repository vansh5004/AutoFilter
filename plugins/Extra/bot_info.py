# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackContext
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters


# def plan(update: Update, context: CallbackContext) -> None:
@Client.on_message(filters.private & filters.command(["bot_info"]))
async def bot_info(client,message):
    # Replace the following placeholders with your actual values
    button_text = '𝑩𝑼𝒀 𝑹𝑬𝑷𝑶 𝑰𝑵 𝑪𝑯𝑬𝑨𝑷 𝑷𝑹𝑰𝑪𝑬'
    photo_url = 'https://graph.org/file/21c9e45d8e50442b24707.jpg'
    plan_text = '𝑩𝑶𝑻 𝑭𝑬𝑨𝑻𝑼𝑹𝑬\n\n1. 𝑷𝑳𝑨𝑵 𝑨𝑵𝑫 𝑴𝒀𝑷𝑳𝑨𝑵 𝑪𝑶𝑴𝑴𝑨𝑵𝑫 𝑨𝑫𝑫𝑬𝑫\n2. 𝑩𝑶𝑻_𝑰𝑵𝑭𝑶 𝑨𝑵𝑫 𝑹𝑬𝑭𝑬𝑹 𝑪𝑶𝑴𝑴𝑨𝑵𝑫 𝑨𝑫𝑫𝑬𝑫\n3. 𝑽𝑬𝑹𝑰𝑭𝒀 𝑶𝑵 𝑨𝑵𝑫 𝑶𝑭𝑭 𝑭𝑬𝑨𝑻𝑼𝑹𝑬 𝑨𝑫𝑫𝑬𝑫\n4. 𝑹𝑬𝑸𝑼𝑬𝑺𝑻 𝑻𝑶 𝑱𝑶𝑰𝑵 𝑪𝑯𝑨𝑵𝑵𝑬𝑳\n5. 𝑰𝑵𝑺𝑻𝑨𝑮𝑹𝑨𝑴 𝑹𝑬𝑬𝑳 𝑫𝑶𝑾𝑵𝑳𝑶𝑨𝑫𝑬𝑹\n6. 𝑨𝑰,𝑾𝑬𝑨𝑻𝑯𝑬𝑹,𝑪𝑶𝑼𝑵𝑻𝑹𝒀,,+12 𝑴𝑶𝑹𝑬\n7. 𝑺𝑯𝑶𝑹𝑻 𝑼𝑹𝑳 𝑭𝑬𝑨𝑻𝑼𝑹𝑬\n8. 𝑴𝑶𝑹𝑬 𝑭𝑬𝑨𝑻𝑼𝑹𝑬 𝑨𝑫𝑫𝑬𝑫 𝑪𝑯𝑬𝑪𝑲 𝑵𝑶𝑾\n\n𝑷𝒓𝒊𝒄𝒆 - 𝒅𝒊𝒔𝒄𝒖𝒔𝒔𝒊𝒐𝒏\n𝑪𝒐𝒏𝒕𝒂𝒄𝒕 𝑩𝒐𝒕 & 𝑹𝒆𝒑𝒐 𝑶𝒘𝒏𝒆𝒓 - @NONE_090'  # Add your plan details here

    # Create an inline keyboard with the buy plan button
    keyboard = [[InlineKeyboardButton(button_text, url='https://t.me/none_090')
                ],[
               InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆",callback_data = "close_data")
                ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the plan details, photo, and the buy plan button
    await client.send_photo(chat_id=message.chat.id,photo=photo_url, caption=plan_text, reply_markup=reply_markup)
