import telebot
from config import BOT_TOKEN, SPREADSHEET_ID, INOUT_ID, RANGE_NAME, RANGE_INOUT, RANGE_STOK, LIST_ID, RANGE_LIST
from stok import handle_stok
from inout import handle_inout
from start import handle_help, handle_start
from list import handle_list
from delete import schedule_deletion
from master import handle_refresh, handle_message
from extra.wa import wa_handler 
from extra.p import ping
from cache import reset_cache
from extra.log import send_log_to_channel

bot = telebot.TeleBot(BOT_TOKEN)

@bot.callback_query_handler(func=lambda call: call.data == 'delete')
def handle_delete_callback(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    schedule_deletion(bot, chat_id, message_id)
    

@bot.message_handler(commands=['ping'])
def ping_handler(message):
    #bot.reply_to(message, 'Pong!')
    ping(bot, message)
    send_log_to_channel(bot, message.from_user, message.text)  # Rekam pesan
    
@bot.message_handler(commands=['p'])
def p_handler(message):
    #bot.reply_to(message, 'Pong!')
    ping(bot, message)
    send_log_to_channel(bot, message.from_user, message.text)  # Rekam pesan
    

# Command handler untuk /wa
@bot.message_handler(commands=['wa'])
def handle_wa(message):
    wa_handler(bot, message)
    send_log_to_channel(bot, message.from_user, message.text)  # Rekam pesan

@bot.message_handler(commands=['start'])
def send_welcome(message):
    handle_start(bot, message)
    send_log_to_channel(bot, message.from_user, message.text)  # Rekam pesan

@bot.message_handler(commands=['help'])
def send_help(message):
    handle_help(bot, message)
@bot.callback_query_handler(func=lambda call: call.data == 'help')
def callback_help(call):handle_help(bot, call.message)

@bot.callback_query_handler(func=lambda call: call.data == 'refresh')
def callback_refresh(call):
    handle_refresh(bot, call.message)

@bot.message_handler(commands=['refresh'])
def refresh_cache(message):
    result_message = reset_cache()  # Memanggil reset_cache() dan menyimpan pesan hasil
    bot.reply_to(message, result_message)  # Mengirim pesan hasil ke pengguna

@bot.message_handler(func=lambda message: message.text.startswith(('. ','/inout')))
def inout_handler(message):
    handle_inout(bot, message, INOUT_ID, RANGE_INOUT)

@bot.message_handler(func=lambda message: message.text.startswith(('.stok ', '/stok')))
def stok(message):
    handle_stok(bot, message, SPREADSHEET_ID, RANGE_STOK)
    send_log_to_channel(bot, message.from_user, message.text)  # Rekam pesan

@bot.message_handler(func=lambda message: message.text.startswith(('.list ','/list')))
def list(message):
    handle_list(bot, message, LIST_ID, RANGE_LIST)

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    handle_message(bot, message, SPREADSHEET_ID, RANGE_NAME)

if __name__ == "__main__":
    bot_info = bot.get_me()
    bot_name = bot_info.first_name

    print(f"Bot '{bot_name}' berjalan 🔴🔴🔴⚪⚪")
    
    print("Starting bot polling...")
    #print("Bot berjalan 🔴🔴🔴⚪⚪")
    #bot.polling()
    #print("Starting bot polling...")
try:
    bot.polling(non_stop=True)
except Exception as e:
    print(f"Error occurred: {e}")
    
    