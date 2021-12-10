import telebot
from telebot import types

TOKEN = '2132519709:AAECAFbn_KE7L9v3ETmeAC31d56CPaEuCRA'
bot = telebot.TeleBot(TOKEN)
# keyboard = types.ReplyKeyboardMarkup()
# bt1 = types.KeyboardButton("YES")
# bt2 = types.KeyboardButton("NO")
# keyboard.add(bt1, bt2)
keyboard = types.InlineKeyboardMarkup()
bt1 = types.InlineKeyboardButton("-YES-", callback_data="YES")
bt2 = types.InlineKeyboardButton("-NO-", callback_data="NO")
keyboard.add(bt1, bt2)

@bot.message_handler(commands=["start"])
def send_hello(message):
    print(message)
    chat_id = message.chat.id
    bot.send_message(
        chat_id,
        "Your name is SADYR?",
        reply_markup=keyboard
    )

# @bot.message_handler(content_types=["text"])
# def privet(message):
#     chat_id = message.chat.id
#     if message.text == "YES":
#         bot.send_message(chat_id, "HELLO SADYR")
#     else:
#         bot.send_message(chat_id, "SORRY")
#         bot.send_sticker(chat_id, "CAACAgEAAxkBAAEDWGlhnPPpE2G_k6j_AkroaAiIWaQaNAACrAADBJKxROVZutNmiOpbIgQ")

@bot.callback_query_handler(func=lambda callback: True)
def privet(callback):
    chat_id = callback.message.chat.id
    if callback.data == "YES":
        bot.send_message(chat_id, "HELLO SADYR")
    else:
        bot.send_message(chat_id, "SORRY")
        bot.send_sticker(chat_id, "CAACAgEAAxkBAAEDWGlhnPPpE2G_k6j_AkroaAiIWaQaNAACrAADBJKxROVZutNmiOpbIgQ")

bot.polling()