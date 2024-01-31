# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackContext
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters


# def plan(update: Update, context: CallbackContext) -> None:
@Client.on_message(filters.private & filters.command(["plan"]))
async def plan(client,message):
    # Replace the following placeholders with your actual values
    button_text = '𝑩𝑼𝒀 𝑷𝑳𝑨𝑵'
    photo_url = 'https://graph.org/file/f8c26a2bda2c9ca9c6871.jpg'
    plan_text = '🎖️ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs\n\n● 10₹ ➛ ʙʀᴏɴᴢᴇ ᴘʟᴀɴ » 7 ᴅᴀʏꜱ\n● 60₹ ➛ ꜱɪʟᴠᴇʀ ᴘʟᴀɴ » 30 ᴅᴀʏꜱ\n● 180₹ ➛ ɢᴏʟᴅ ᴘʟᴀɴ » 90 ᴅᴀʏꜱ\n● 250₹ ➛ ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ » 180 ᴅᴀʏꜱ\n● 400₹ ➛ ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ » 365 ᴅᴀʏꜱ\n\n💵 ᴜᴘɪ ɪᴅ - <code>vansh009@fam</code>\n\n⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ: /myplan\n\n‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.'  # Add your plan details here

    # Create an inline keyboard with the buy plan button
    keyboard = [[InlineKeyboardButton(button_text, url='https://t.me/none_090')
                ],[
               InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆",callback_data = "close_data")
                ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the plan details, photo, and the buy plan button
    await client.send_photo(chat_id=message.chat.id,photo=photo_url, caption=plan_text, reply_markup=reply_markup)

