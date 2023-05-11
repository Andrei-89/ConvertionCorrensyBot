#Для отправки запросов к API описать класс со статическим методом get_price(),
# который принимает три аргумента:
# имя валюты, цену на которую надо узнать,
# — base, имя валюты, цену в которой надо узнать,
# — quote, количество переводимой валюты
# — amount и возвращает нужную сумму в валюте.

import requests
import json
from config import currency

class ConvertionExeption(Exception):
    pass

class CorrensyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: float = 1):
        try:
            quote_ticker = currency[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}, '
                                     f'посмотреть список допустимых валют /values')
        try:
            base_ticker = currency[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}, '
                                     f'посмотреть список допустимых валют /values')
        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты - {quote}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать количество {amount}')
        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}').content
        total_result = json.loads(r)[currency[base]]*int(amount)
        return total_result



# class get_price():
#     def __init__(self, guote, amount):
