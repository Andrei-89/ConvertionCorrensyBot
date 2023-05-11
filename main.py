import telebot
from config import TOKEN, currency
from extensions import ConvertionExeption, CorrensyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_cmd(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Приветстрвую, {message.chat.username}!\nВведите данные:")

@bot.message_handler(commands=['help'])
def help_info(message: telebot.types.Message):
    text = f"Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).\n"\
           f"Отправте сообщение боту в виде \n*<имя валюты цену которой он хочет узнать>" \
           f"\n*<имя валюты в которой надо узнать цену первой валюты> \n*<количество первой валюты>.\n" \
           f"Например:\nдоллар рубль 100\nУвидеть список всех доступных валют /values"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def currency_cmd(message: telebot.types.Message):
    text = 'Досупные валюты:'
    for key in currency.keys():
        text += '\n' + key
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def currency_cmd(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionExeption('Введено не верное количество параметров')
    except Exception as e:
        bot.reply_to(message, f"Ошибка пользователя.\n{e} /help")
    else:
        try:
            quote, base, amount = values
            total_base = CorrensyConverter.get_price(quote, base, amount)
        except ConvertionExeption as e:
            bot.reply_to(message, f"Ошибка пользователя.\n/help\n{e}")
        else:
            text = f'Цена валюты {currency[quote]} в количестве {amount} в {currency[base]} = {total_base} {currency[base]}'
            bot.send_message(message.chat.id, text)


    # adress = f'https://min-api.cryptocompare.com/data/price?fsym={quote}&tsyms={base}'
    # quote, base = message.text.split(' ')



bot.polling(none_stop=True)

