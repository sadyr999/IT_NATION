import requests
import telebot
from bs4 import BeautifulSoup

TOKEN = '2132519709:AAECAFbn_KE7L9v3ETmeAC31d56CPaEuCRA'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

welcome_text = '''Здраствуйте, приветсвуем вас на нашем онлайн магазине!
                  Выберите супермаркет!'''
shop_list = [
    {'name': 'Globus'},
    {'name': 'Народный'},
    {'name': 'Фрунзе'},
]
globus_url = "https://globus-online.kg/catalog/"


@bot.message_handler(content_types=['text'])
def auto_handler(message):
    marсup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    marсup.row(
        shop_list[0]['name'],
        shop_list[1]['name'],
        shop_list[2]['name'],
    )

    if message.text.lower() == 'hello':
        bot.reply_to(message=message, text=welcome_text, reply_markup=marсup)

    if message.text == shop_list[0]['name']:
        response = requests.get(globus_url)
        soup = BeautifulSoup(response.text, 'lxml')
        ul = soup.find('ul', 'row list-unstyled')
        category_list = ul.find_all('a', 'parent')
        marcup = generate_globus_product_category_btn(category_list)

        bot.send_message(
            chat_id=message.chat.id, text='Test', reply_markup=marcup
        )

    if message.text == shop_list[1]['name']:
        print(message.text)
    if message.text == shop_list[2]['name']:
        print(message.text)


def generate_globus_product_category_btn(category_list):
    category_names = [name.text for name in category_list]
    marcup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for category_name in category_names:
        marcup.add(category_name)
    return marcup


bot.infinity_polling()
