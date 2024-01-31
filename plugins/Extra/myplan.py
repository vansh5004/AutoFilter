from os import environ
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from pyrogram import Client , filters
from pyrogram import types
from pyrogram.types import Update, Message
from telegram.ext import CallbackContext
from datetime import datetime, timedelta
from info import PREMIUM_USER


# Define your global variables to store user IDs based on plans
trial_users = set()
gold_users = set()
bronze_users = set()
diamond_users = set()

# Make VANSH_PREMIUM global
global PREMIUM_USER
# PREMIUM_USER = set(int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split())


@Client.on_message(filters.private & filters.command(["addpremium"]))
async def addpremium(client, message, **kwargs):
    
    global trial_users, gold_users, bronze_users, diamond_users
    trial_users = dict(trial_users)
    gold_users = dict(gold_users)
    bronze_users = dict(bronze_users)
    diamond_users = dict(diamond_users)
    
    # Check if the command is sent by an admin
    if message.from_user.id not in YOUR_ADMIN_IDS:
        await message.reply_text('You are not authorized to use this command.')
        return

    # Get user input
    try:
        command_args = message.text.split(" ", 2)  # Split into three parts: /addpremium, plan, and user_id
        plan = command_args[1].strip().upper()
        user_id = int(command_args[2].strip())
    except (IndexError, ValueError):
        await message.reply_text('Invalid command format. Use /addpremium {plan}and{user_id}')
        return


    # Update user IDs based on the specified plan
    global current_time
    current_time = datetime.now()

    
    if plan == 'TRIAL':
        trial_users[user_id] = current_time
    elif plan == 'GOLD':
        gold_users[user_id] = current_time
    elif plan == 'BRONZE':
        bronze_users[user_id] = current_time
    elif plan == 'DIAMOND':
        diamond_users[user_id] = current_time
    else:
        await message.reply_text('Invalid plan. Supported plans are TRIAL, GOLD, BRONZE, DIAMOND.')
        return

    # Update the combined list only with new user IDs
    new_user_ids = {user_id} - PREMIUM_USER
    PREMIUM_USER.update(new_user_ids)

    # Format new_user_ids for the confirmation message
    formatted_user_id = f"'{user_id}'"

    

    # Send a confirmation message
    await message.reply_text(f'Successfully added {plan} plan for user {user_id}.')


@Client.on_message(filters.private & filters.command(["myplan"]))
async def myplan(client, message):
    user_id = message.from_user.id
  #  user_id = update.from_user.id

    # Convert sets to dictionaries
    global trial_users, gold_users, bronze_users, diamond_users
    trial_users_dict = dict(trial_users)
    gold_users_dict = dict(gold_users)
    bronze_users_dict = dict(bronze_users)
    diamond_users_dict = dict(diamond_users)
    

    if user_id in trial_users_dict:
        remaining_time = (trial_users_dict[user_id] + timedelta(days=1)) - datetime.now()
        await message.reply_text(f'Your plan is TRIAL. Expires in {remaining_time}.')
    elif user_id in gold_users_dict:
        remaining_time = (gold_users_dict[user_id] + timedelta(days=90)) - datetime.now()
        await message.reply_text(f'Your plan is GOLD. Expires in {remaining_time}.')
    elif user_id in bronze_users_dict:
        remaining_time = (bronze_users_dict[user_id] + timedelta(days=30)) - datetime.now()
        await message.reply_text(f'Your plan is BRONZE. Expires in {remaining_time}.')
    elif user_id in diamond_users_dict:
        remaining_time = (diamond_users_dict[user_id] + timedelta(days=180)) - datetime.now()
        await message.reply_text(f'Your plan is DIAMOND. Expires in {remaining_time}.')
    else:
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton('𝑩𝑼𝒀 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 𝑷𝑳𝑨𝑵', callback_data='buy_premium')
                                         ],[
                    InlineKeyboardButton('𝑪𝑳𝑶𝑺𝑬', callback_data='close_data')
                         ]])


        
        await message.reply_text('𝒀𝑶𝑼 𝑫𝑶 𝑵𝑶𝑻 𝑯𝑨𝑽𝑬 𝑨𝑵𝒀 𝑨𝑪𝑻𝑰𝑽𝑬 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 𝑷𝑳𝑨𝑵𝑺, 𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑻𝑨𝑲𝑬 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 𝑻𝑯𝑬𝑵 𝑪𝑳𝑰𝑪𝑲 𝑶𝑵 𝑩𝑬𝑳𝑶𝑾 𝑩𝑼𝑻𝑻𝑶𝑵', reply_markup=keyboard)
       # update.message.reply_text('𝑯𝑬𝒀 {message.from_user.mention},\n\n𝒀𝑶𝑼 𝑫𝑶 𝑵𝑶𝑻 𝑯𝑨𝑽𝑬 𝑨𝑵𝒀 𝑨𝑪𝑻𝑰𝑽𝑬 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 𝑷𝑳𝑨𝑵𝑺, 𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑻𝑨𝑲𝑬 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 𝑻𝑯𝑬𝑵 𝑪𝑳𝑰𝑪𝑲 𝑶𝑵 𝑩𝑬𝑳𝑶𝑾 𝑩𝑼𝑻𝑻𝑶𝑵', reply_markup=keyboard)

# Set up the Telegram bot
# YOUR_BOT_TOKEN = 'your_bot_token'
YOUR_ADMIN_IDS = [2020224264]  # Replace with your admin IDs

from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters


# def plan(update: Update, context: CallbackContext) -> None:
@Client.on_callback_query(filters.regex('buy_premium'))
async def buy_premium(client, callback_query):
    button_text = '𝑩𝑼𝒀 𝑷𝑳𝑨𝑵'
    photo_url = 'https://graph.org/file/f8c26a2bda2c9ca9c6871.jpg'
    plan_text = '🎖️ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs\n\n● 10₹ ➛ ʙʀᴏɴᴢᴇ ᴘʟᴀɴ » 7 ᴅᴀʏꜱ\n● 60₹ ➛ ꜱɪʟᴠᴇʀ ᴘʟᴀɴ » 30 ᴅᴀʏꜱ\n● 180₹ ➛ ɢᴏʟᴅ ᴘʟᴀɴ » 90 ᴅᴀʏꜱ\n● 250₹ ➛ ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ » 180 ᴅᴀʏꜱ\n● 400₹ ➛ ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ » 365 ᴅᴀʏꜱ\n\n💵 ᴜᴘɪ ɪᴅ - <code>vansh009@fam</code>\n\n⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ: /myplan\n\n‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.'

    # Create an inline keyboard with the buy plan button
    keyboard = [[InlineKeyboardButton(button_text, url='https://t.me/none_090')],
                [InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆", callback_data="close_data")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the plan details, photo, and the buy plan button
    await callback_query.message.reply_photo(photo=photo_url, caption=plan_text, reply_markup=reply_markup)

    # Answer the callback query to close the inline keyboard
    await callback_query.answer()


# Function to convert sets to dictionaries
def convert_sets_to_dicts():
    global trial_users, gold_users, bronze_users, diamond_users
    trial_users = dict(trial_users)
    gold_users = dict(gold_users)
    bronze_users = dict(bronze_users)
    diamond_users = dict(diamond_users)
    

# Function to remove a user's plan
def remove_plan(plan_users, user_id):
    plan_users = dict(plan_users)  # Convert set to dictionary
    if user_id in plan_users:
        del plan_users[user_id]
        return True
    return False

# Define the /removepremium command
@Client.on_message(filters.private & filters.command(["removepremium"]))
async def removepremium(client, message):
    # Check if the command is sent by an admin
    if message.from_user.id not in YOUR_ADMIN_IDS:
        await message.reply_text('You are not authorized to use this command.')
        return

    # Convert sets to dictionaries
    convert_sets_to_dicts()

    # Get user input
    try:
        command_args = message.text.split(" ", 2)
        plan = command_args[1].strip().upper()
        user_id = int(command_args[2].strip())
    except (IndexError, ValueError):
        await message.reply_text('Invalid command format. Use /removepremium {plan} {user_id}')
        return

    # Validate plan
    if plan not in ['TRIAL', 'GOLD', 'BRONZE', 'DIAMOND']:
        await message.reply_text('Invalid plan name. Supported plans are TRIAL, GOLD, BRONZE, DIAMOND.')
        return

    # Update user plan dictionaries
    convert_sets_to_dicts()

    # Remove user's plan based on the specified plan name
    success = remove_plan(eval(f'{plan.lower()}_users'), user_id)

    # Remove user's plan based on the specified plan name
 #   if plan == 'TRIAL':
 #       success = remove_plan(trial_users, user_id)
 #   elif plan == 'GOLD':
 #       success = remove_plan(gold_users, user_id)
 #   elif plan == 'BRONZE':
 #       success = remove_plan(bronze_users, user_id)
 #   elif plan == 'DIAMOND':
 #       success = remove_plan(diamond_users, user_id)
 #   else:
 #       await message.reply_text('Invalid plan name. Supported plans are TRIAL, GOLD, BRONZE, DIAMOND.')
 #       return

    # Send a confirmation message
    if success:
        await message.reply_text(f'Successfully removed {plan} plan for user {user_id}.')
    else:
        await message.reply_text(f'The user with ID {user_id} does not have an active {plan} plan.')


# Define the /premium_users command
@Client.on_message(filters.private & filters.command(["premium_users"]))
async def premium_users(client, message):
    # Check if the command is sent by an admin
    if message.from_user.id not in YOUR_ADMIN_IDS:
        await message.reply_text('You are not authorized to use this command.')
        return

    # Convert sets to dictionaries
    convert_sets_to_dicts()

    # Prepare a message to display premium users
    premium_users_message = "Premium Users:\n"

    # Check and append TRIAL users
    if trial_users:
        premium_users_message += "\nTRIAL Users:\n"
        for user_id, expiry_time in trial_users.items():
            premium_users_message += f"{user_id} - Expires on {expiry_time}\n"
    else:
        premium_users_message += "No TRIAL users found.\n"

    # Check and append GOLD users
    if gold_users:
        premium_users_message += "\nGOLD Users:\n"
        for user_id, expiry_time in gold_users.items():
            premium_users_message += f"{user_id} - Expires on {expiry_time}\n"
    else:
        premium_users_message += "No GOLD users found.\n"

    # Check and append BRONZE users
    if bronze_users:
        premium_users_message += "\nBRONZE Users:\n"
        for user_id, expiry_time in bronze_users.items():
            premium_users_message += f"{user_id} - Expires on {expiry_time}\n"
    else:
        premium_users_message += "No BRONZE users found.\n"

    # Check and append DIAMOND users
    if diamond_users:
        premium_users_message += "\nDIAMOND Users:\n"
        for user_id, expiry_time in diamond_users.items():
            premium_users_message += f"{user_id} - Expires on {expiry_time}\n"
    else:
        premium_users_message += "No DIAMOND users found.\n"

    # Send the premium users message as a direct message to the admin
    admin_id = message.from_user.id
    await client.send_message(chat_id=admin_id, text=premium_users_message)
    
