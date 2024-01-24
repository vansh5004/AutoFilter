from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters
import info PREMIUM_USER
from datetime import datetime, timedelta
import os
# from plugins.helper.fotnt_string import Fonts
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Define the plans and prices along with their durations (in days)
plans_durations = {
    '7days': {'price': '20rs', 'duration': 7},
    '14days': {'price': '35rs', 'duration': 14},
    '1month': {'price': '60rs', 'duration': 30},  # Assuming 1 month has 30 days
    '3months': {'price': '120rs', 'duration': 90},  # Assuming 1 month has 30 days
}

# Admin user id (replace with your admin user id)
ADMIN_USER_ID = 123456789

# Command handler for /plan command
@Client.on_message(filters.private & filters.command(["plan"]))
def plan(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id

    # Send the photo
    photo_url = 'https://graph.org/file/66e0fc2970bda9316dd95.jpg'  # Replace with the actual URL of your photo
    context.bot.send_photo(chat_id, photo=photo_url, caption='Available Plans:')

    # Create an inline keyboard with the "Buy Plan" button
    inline_keyboard = [
        [InlineKeyboardButton("Buy Plan", callback_data='buy_plan')],
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard)

    # Send the keyboard along with the message
    update.message.reply_text(get_plans_text(), reply_markup=reply_markup)

# Callback handler for inline button clicks
def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    chat_id = query.message.chat_id

    if query.data == 'buy_plan':
        # Create a new inline keyboard with two options
        inline_keyboard = [
            [InlineKeyboardButton("Option 1", callback_data='option1')],
            [InlineKeyboardButton("Option 2", callback_data='option2')],
        ]
        reply_markup = InlineKeyboardMarkup(inline_keyboard)

        # Edit the message to show the new inline keyboard
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=query.message.message_id,
            text='Choose an option:',
            reply_markup=reply_markup
        )

# Command handler for /myplan command
@Client.on_message(filters.private & filters.command(["myplan"]))
def my_plan(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)

    if user_id in info.PREMIUM_USERS:
        # User has a premium plan
        plan_name = 'Premium Plan'
        plan_duration = info.PREMIUM_USERS[user_id]['duration']
        plan_expiry = info.PREMIUM_USERS[user_id]['purchase_date'] + timedelta(days=plan_duration)

        update.message.reply_text(f'Your Plan: {plan_name}\nExpiry Date: {plan_expiry.strftime("%Y-%m-%d")}')
    else:
        # User does not have a premium plan
        update.message.reply_text('You do not have a premium plan. Click the button below to buy a plan.')
        
        # Create an inline keyboard with the "Buy Plan" button
        inline_keyboard = [
            [InlineKeyboardButton("Buy Plan", url=f'https/t.me/none_090')],
        ]
        reply_markup = InlineKeyboardMarkup(inline_keyboard)

        # Send the keyboard along with the message
        update.message.reply_text(get_plans_text(), reply_markup=reply_markup)

def get_plans_text() -> str:
    plan_text = "Available Plans:\n"
    for plan, details in plans_durations.items():
        plan_text += f"{plan}: {details['price']} ({details['duration']} days)\n"
    return plan_text

# Command handler for /add_premium command (admin only)
@Client.on_message(filters.private & filters.command(["add_premium"]))
def add_premium(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id == ADMIN_USER_ID:
        # Admin user can add users to premium plan
        context.bot.send_message(update.message.chat_id, 'Admin, please select a plan to add the user to.')
        
        # Create an inline keyboard with plan options
        inline_keyboard = [
            [InlineKeyboardButton(plan, callback_data=f'add_plan_{plan}')] for plan in plans_durations
        ]
        reply_markup = InlineKeyboardMarkup(inline_keyboard)

        # Send the keyboard along with the message
        update.message.reply_text(get_plans_text(), reply_markup=reply_markup)
    else:
        update.message.reply_text('You do not have permission to use this command.')

# Callback handler for inline button clicks to add a premium plan
@Client.on_message(filters.private & filters.command(["add_plan"]))
def add_plan(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    chat_id = query.message.chat_id
    plan_name = query.data.split('_')[-1]

    if plan_name in plans_durations:
        # Plan selected by the admin
        user_id = str(context.user_data['add_premium_user_id'])

        # Add the user to the premium user list
        info.PREMIUM_USERS[user_id] = {
            'plan': plan_name,
            'duration': plans_durations[plan_name]['duration'],
            'purchase_date': datetime.now(),
        }

        # Send a thank you message to the user
        context.bot.send_message(user_id, f'Thank you for purchasing the {plan_name} plan! Your plan will expire on {info.PREMIUM_USERS[user_id]["purchase_date"] + timedelta(days=info.PREMIUM_USERS[user_id]["duration"])}.')

        # Clear the user data
        del context.user_data['add_premium_user_id']

        # Inform the admin
        context.bot.send_message(chat_id, f'The user with Telegram ID {user_id} has been added to the {plan_name} plan.')
    else:
        context.bot.send_message(chat_id, 'Invalid plan selection.')
