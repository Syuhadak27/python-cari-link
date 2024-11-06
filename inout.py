import re
import time
import threading
from telebot import TeleBot
from Button import create_refresh_button
from delete import schedule_deletion
from cache import get_google_sheet_data, cached_inout_data, cache_timestamps, CACHE_EXPIRY
from extra.log import send_log_to_channel_inout

def handle_inout(bot, message, INOUT_ID, RANGE_INOUT):
    global cached_inout_data
    query = message.text[1:]  # Menghapus titik di awal
    send_log_to_channel_inout(bot, message.from_user, query)

    if not query:
        msg = bot.reply_to(message, "Tidak bisa tanpa kata kunci")
        schedule_deletion(bot, message.chat.id, msg.message_id, 2)
        schedule_deletion(bot, message.chat.id, message.message_id, 2)
        return

    query_parts = query.split()

    if cached_inout_data is None or time.time() - cache_timestamps["inout"] > CACHE_EXPIRY:
        cached_inout_data = get_google_sheet_data(INOUT_ID, RANGE_INOUT)
        cache_timestamps["inout"] = time.time()

    # Filter data berdasarkan kata kunci
    filtered_data = [
        row for row in cached_inout_data 
        if all(re.search(re.escape(part), ' '.join(row), re.IGNORECASE) for part in query_parts)
    ]

    # Fungsi untuk membersihkan data numerik dari karakter non-digit
    def clean_number(value):
        try:
            # Hapus semua karakter selain angka dan titik desimal
            cleaned_value = re.sub(r"[^\d.]", "", value)
            return float(cleaned_value) if cleaned_value else 0
        except ValueError:
            return 0

    # Menghitung jumlah kolom 4 dan kolom 5 dengan pembersihan data
    sum_kolom_4 = sum(clean_number(row[3]) for row in filtered_data)
    sum_kolom_5 = sum(clean_number(row[4]) for row in filtered_data)

    # Membangun respon dengan format baru
    response = f"Kata Kunci: <code>{query}</code>\n"
    response += f"Ket:\n🟢 Masuk -- {int(sum_kolom_4)} pcs\n🔴 Keluar -- {int(sum_kolom_5)} pcs\n\n"

    if filtered_data:
        for row in filtered_data:
            # Format kolom pertama dengan <pre><code> agar bisa di-copy dengan sekali klik
            response += f"<blockquote>🔄<code>{row[0]}</code> • " + ' • '.join(row[1:]) + "</blockquote>\n"
        schedule_deletion(bot, message.chat.id, message.message_id, 2)
    else:
        response = "Salah kata kunci dan tidak ditemukan😜\n\nUntuk memperbarui data tekan tombol di bawah."
        msg = bot.send_message(message.chat.id, response, reply_markup=create_refresh_button(), parse_mode='HTML')
        schedule_deletion(bot, message.chat.id, msg.message_id, 2)
        schedule_deletion(bot, message.chat.id, message.message_id, 2)
        return

    def send_long_message(chat_id, message_text):
        max_length = 4096
        # Memastikan pesan tidak terpotong di tengah tag HTML
        while message_text:
            part = message_text[:max_length]
            if len(part) == max_length:
                last_index = part.rfind("</blockquote>") + len("</blockquote>")
                if last_index > 0:
                    part = message_text[:last_index]
                else:
                    part = message_text[:max_length]
            bot.send_message(chat_id, part, parse_mode="HTML")
            message_text = message_text[len(part):]

    send_long_message(message.chat.id, response)