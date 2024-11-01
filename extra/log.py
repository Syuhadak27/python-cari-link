from telebot import TeleBot
import time
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

# Muat variabel dari config.env
load_dotenv()

# Ambil CHANNEL_ID dari variabel lingkungan
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

LOG_CHANNEL_ID = CHANNEL_ID  # Ganti dengan ID channel log Anda

# Fungsi untuk mendapatkan waktu GMT+7
def get_gmt7_time():
    gmt7 = timezone(timedelta(hours=7))
    return datetime.now(gmt7).strftime('%Y-%m-%d %H:%M:%S')

def send_log_to_channel(bot: TeleBot, user, query):
    log_message = (
        f"<blockquote>📅 Waktu: {get_gmt7_time()}</blockquote>\n"
        f"<blockquote>👤 Nama Pengguna: {user.first_name} (@{user.username if user.username else 'N/A'})</blockquote>\n"
        f"<blockquote>🔎 Kata yang Dimasukkan: <code>\n{query}</code></blockquote>"
    )
    bot.send_message(LOG_CHANNEL_ID, log_message, parse_mode="HTML")
    
def send_log_to_channel_inout(bot: TeleBot, user, query):
    log_message = (
        f"<blockquote>📅 Waktu: {get_gmt7_time()}</blockquote>\n"
        f"<blockquote>👤 Nama Pengguna: {user.first_name} (@{user.username if user.username else 'N/A'})</blockquote>\n"
        f"<blockquote>🔎 Kata yang Dimasukkan: <code>\n/inout {query}</code></blockquote>"
    )
    bot.send_message(LOG_CHANNEL_ID, log_message, parse_mode="HTML")