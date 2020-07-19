def main():
    data = get_data()
    pass


def get_data():
    number = int(input())
    return


# if __name__ == '__main__':
#     res = main()
#     print(res)
# _____________________________

# import importlib
# from . import my-work
# my_work = importlib.import_module('путь к модулю')

# _________________________________ LOCAL< GLOBAL

COUNTER = 0


def test_local_vars_fun(var, var2):
    return var, var2


def test_local_vars_fun_out_of_scope(a, b):
    pass


def count_words(string, delimiter):
    res_list = string.split(delimiter)
    for item in res_list:
        if item == 'increment':
            global COUNTER
            COUNTER += 1


my_str = 'football, ball, foot, football, increment, increment'
delim = ', '


# count_words(my_str, delim)
# print(COUNTER)


# ____________________ args, kwargs


def some_fun(*args, **kwargs):
    pass


def danger_function(arg, data=None):
    if not data:
        data = []
    data.append(arg)
    return data


# print(danger_function(1))
# print(danger_function(2))
# print(danger_function(3))
# print(danger_function(4))


# ____________  рекурсия


def fib(n):
    if not n:
        return n
    elif n in {1, 2}:
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(100))


def crash():
    return crash()


# ______________ files

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

# with open('test.txt', 'r+') as file, open('cl7.txt', 'w+') as file2:
#     data = file.read()
#     file2.write(data)

import json
from datetime import datetime
# DATA = {
#     'name': 'Vitalii',
#     'age': 24,
#     'updated': str(datetime.now())
# }

# with open('test.json', 'w') as file:
#     json.dump(DATA, file, indent=4)

# with open('test.json', 'r') as file_to_read:
#     data = json.load(file_to_read)
#     print(data)

import requests

resp = requests.get('http://www.mocky.io/v2/5e56aa7030000046d228e971')
data = resp.json()