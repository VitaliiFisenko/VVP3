"""
2 
Написать функцию для сортировки для  списка словарей.

Сортировать по ключу `name`, если такого ключа нету в словаре, то по ключу `lastname`
"""


def sort_func(dict_to_sort):
    if dict_to_sort.get('name'):
        return dict_to_sort['name']
    return dict_to_sort['lastname']


dictionary = {'name': 'Iiuvan', 'lastname': 'Ivanov'}
dictionaries = [dictionary, {'lastname': 'cIvanov'}, {'name': 'Bbvan', 'lastname': 'Bvanov'}]
dictionaries.sort(key=sort_func, reverse=False)
# print(dictionaries)

"""
3
Функции принимают 1 аргумент (list с числами) и возвращает максимальное/минимальное значение. Использовать сортировку 
нельзя.
"""


def get_extremum(my_list):
    return min(my_list), max(my_list)


var = [1, 2, 3, 4, 5, 5, 6, 7]

# print(get_extremum(var))

"""
4 
Написать функцию, которая принимает 1 аргумент — год, и возвращающую True, если год високосный, иначе False
"""
import calendar


def is_leap(year):
    if not isinstance(year, (str, int)):
        return
    if isinstance(year, str) and year.isdigit():
        year = int(year)
    else:
        return
    return calendar.isleap(year)


input_year = '20d1'
input_year1 = 2020
# print(is_leap(input_year))
"""
5
Функция принимает список и должна вернуть True, если все элементы уникальные (не повторяются больше 1 раза),
иначе - False

Желательно (но необезательно) использовать set
"""


def comparator(to_compare):
    return len(to_compare) == len(set(to_compare))


print(comparator(range(1, 15)))
print(comparator([1, 2, 3, 4, 45, 5, 65, 5, 5, 5]))
"""
6
Напишите программу, которая принимает год и возвращает список дат всех понедельников в данном году.

"""

import datetime


def mondays(year):
    my_list = []
    date = datetime.datetime(year, 1, 1)
    while date.year == year:
        if date.strftime("%A") == 'Monday':
            my_list.append(date.strftime("%d-%m-%Y"))
        date += datetime.timedelta(days=1)
    return my_list


my_list = mondays(2019)
for dates in my_list:
    print(dates)

