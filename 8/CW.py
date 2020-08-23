# def test_fun():
#     # print(globals(), 'aaaa')
#     global ATTEMPS  # можно но лучше так не делать
#     ATTEMPS = 1
#     # print(globals())
#
#
# test_fun()
# # print(ATTEMPS)
#
# #  lambda

func = lambda a: a * a  # так плохо

some_array = [1, 2, 3, 4, 5]

out = list(map(lambda i: i * i, some_array))

out = [i * i for i in some_array]
# print(out)
#
# """
# 2
# Написать функцию для сортировки для  списка словарей.
#
# Сортировать по ключу `name`, если такого ключа нету в словаре, то по ключу `lastname`
# """
#
#
# def sort_func(d):
#     return d.get('name') or d.get('lastname')
#
#
# dictionary = {'name': 'Aiuvan', 'lastname': 'Ivanov'}
# dictionaries = [dictionary, {'lastname': 'cIvanov'}, {'name': 'Bbvan', 'lastname': 'Bvanov'}]
# dictionaries.sort(key=lambda d: d.get('name') or d.get('lastname'))
#
#
# # def calc(var_1: int, var_2: int, oper: str) -> int:
# #     operation_dict = {
# #         'add': lambda a, b: a + b,
# #         'div': lambda a, b: a / b,
# #         'mul': lambda a, b: a * b,
# #         'sub': lambda a, b: a - b,
# #     }
# #     if var_2 == 0:
# #         return False
# #     return operation_dict[oper](var_1, var_2)
# #
# #
# # print(calc(2, 0, 'add'))
#
# def calc(var_1: int, var_2: int, key: str) -> int:
#     def add(a, b):
#         return a + b
#
#     def sub(a, b):
#         return a - b
#
#     operation_dict = {
#         '+': add,
#         '-': sub,
#     }
#     return operation_dict[key](var_1, var_2)

# def expects(fun):
#     def wrapper(*args, **kwargs):
#         try:
#             return fun(*args, **kwargs)
#         except ValueError as ex:
#             print(ex, 'aaaaaaa')
#     return wrapper
#
#
# @expects
# def to_int(number):
#     return int(number)
#
# to_int('s')

# import re
# txt = "The rain in Spain"
# # x = re.search("^The.*Spain$", txt)
# # print(x)
# # print(dir(x))

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)


# def first_gen():
#     print('Alarm')
#     for i in range(5):
#         yield i
#         print(i*i)

gen = (i for i in range(5))
print(next(gen))
next(gen)
next(gen)
next(gen)
next(gen)
print(next(gen))



