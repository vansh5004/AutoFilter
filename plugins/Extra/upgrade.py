from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """🎖️ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs
 
● 10₹ ➛ ʙʀᴏɴᴢᴇ ᴘʟᴀɴ » 7 ᴅᴀʏꜱ
● 60₹ ➛ ꜱɪʟᴠᴇʀ ᴘʟᴀɴ » 30 ᴅᴀʏꜱ
● 180₹ ➛ ɢᴏʟᴅ ᴘʟᴀɴ » 90 ᴅᴀʏꜱ
● 250₹ ➛ ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ » 180 ᴅᴀʏꜱ
● 400₹ ➛ ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ » 365 ᴅᴀʏꜱ

💵 ᴜᴘɪ ɪᴅ - vansh009@fam
📸 ǫʀ ᴄᴏᴅᴇ - ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ

⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan
‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ."""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Buy Now",url = "https://t.me/none_090")
           ],[
                InlineKeyboardButton("Cancel",callback_data = "close_data")]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """🎖️ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs

● 10₹ ➛ ʙʀᴏɴᴢᴇ ᴘʟᴀɴ » 7 ᴅᴀʏꜱ
● 60₹ ➛ ꜱɪʟᴠᴇʀ ᴘʟᴀɴ » 30 ᴅᴀʏꜱ
● 180₹ ➛ ɢᴏʟᴅ ᴘʟᴀɴ » 90 ᴅᴀʏꜱ
● 250₹ ➛ ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ » 180 ᴅᴀʏꜱ
● 400₹ ➛ ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ » 365 ᴅᴀʏꜱ

💵 ᴜᴘɪ ɪᴅ - vansh009@fam
📸 ǫʀ ᴄᴏᴅᴇ - ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ

⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan
‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ."""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Buy Now",url = "https://t.me/none_090")
           ],[
                InlineKeyboardButton("Cancel",callback_data = "close_data")]])
	await message.reply_text(text = text,reply_markup = keybord)
