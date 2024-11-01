
import os
from telebot import TeleBot, types
from dotenv import load_dotenv

# Muat variabel dari config.env
load_dotenv()

# Ambil CHANNEL_ID dari variabel lingkungan
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

def get_channel_info(bot: TeleBot):
    try:
        return bot.get_chat(CHANNEL_ID)
    except:
        return None

def check_membership(bot: TeleBot, user_id):
    try:
        member_status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return member_status in ["member", "administrator", "creator"]
    except:
        return False

def prompt_join_channel(bot: TeleBot, chat_id):
    channel_info = get_channel_info(bot)
    
    if channel_info and channel_info.username:
        join_button = types.InlineKeyboardMarkup()
        join_button.add(types.InlineKeyboardButton(f" {channel_info.title}", url=f"https://t.me/{channel_info.username}"))
        msg = bot.send_message(
            chat_id,
            f"Anda harus join channel {channel_info.title} terlebih dahulu untuk menggunakan bot ini.",
            reply_markup=join_button
        )
        return msg
    else:
        msg = bot.send_message(
            chat_id,
            "Maaf, tidak dapat mengakses channel saat ini. Coba lagi nanti."
        )
        return msg