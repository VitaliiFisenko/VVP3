""""""
from datetime import datetime

"""
Напишите программу, которая выводит все кратные 5 числа, между двумя, которые введет пользователь
"""


def get_five(start, stop):
    while start % 5 != 0:
        start += 1
    return list(range(start, stop, 5))


"""

Программа должна запрашивать у пользователя сумму в гривнах (uah), и тип валюты (usd/euro) для обмена.

Если валюта не из списка, печатаем ошибку.

Если все ок, печатаем сумму в запрашиваемой валюте по курсу.
"""
CURRENCY_MAP = {
    'UAN': 10,
    'USD': 20,
    'EUR': 30,
}


def converter(summ, curr_type):
    if curr_type not in CURRENCY_MAP:
        raise KeyError
    return summ / CURRENCY_MAP[curr_type]


#
# print(converter(1000000, 'EUR'))
# print(converter(1000000, 'EUR'))

"""
Написать функцию, которая принимает 1 параметр (строка) — день-месяц-год час:минуты:секунды ("10-10-2019 00:24:12").

Вернуть True, если время и дата валидные, иначе False.

Валидная дата - это дата, которая реально может быть.
"""


def date_converter(date_str, date_format):
    try:
        datetime.strptime(date_str, date_format)
    except Exception:
        return False
    return True


# print(date_converter("0087", '%Y'))

"""
Написать функцию, которая на вход принимает число и возвращает сумму всех его цифр. Операцию повторять до тех пор, 
пока не останется одна цифра.


Например:

дано: 5349
5 + 3 + 4 + 9 = 21 2 + 1= 3
вывод: 3
"""
# num = '5349'
# while len(str(num)) != 1:
#     num = str(num)
#     num = int(num[:-1]) + int(num[-1])
# print(num)


"""
Написать функцию которая принимает цвет  
rgb в формате 255, 0, 0 и возвращает цвет в  шестнадцатеричном формате ff0000. То есть 255, 66, 180 вернула ff42b4
"""
#  нужно скинуть
"""

Сложный таск

Написасть кастомное логирование
"""
import time


def logger(func, *args, **kwargs):
    with open('log.txt', 'a') as file:
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        res_str = f"{func.__name__} {args} {kwargs} {list(res)} {stop - start}"
        file.write(res_str)
    return res


logger(map, int, ['1', '2'])

"""
написать пакет (питоновский файл), у которого есть 2 функции:

функция, которая принимает обычное число (int) и возвращает римское число (str)
римское_число = ваша_функция(12)
принт(римское_число)
>>> 'XII'
функция, которая принимает римское число (str) и возвращает обычное число (int)
обычное_число = ваша_функция('XII')
принт(обычное_число)
>>> 12
"""
CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
              (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
              (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def from_roman(n):
    result = ''
    for arabic, roman in CONV_TABLE:
        result += n // arabic * roman
        n %= arabic
    return result


def from_arabic(txt):
    txt = txt.upper()
    ret = 0
    for arab, roman in CONV_TABLE:
        while txt.startswith(roman):
            ret += arab
            txt = txt[len(roman):]
    return ret
