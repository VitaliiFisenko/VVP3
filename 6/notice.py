import this


def do(var):
    if var == 3:
        pass
    elif var == 5:
        pass
    elif var == 6:
        pass
    elif var == 7:
        pass
    return

# HW 7 task 2

from collections import Counter


# def converter(string, delimiter):
#     return Counter(string.split(delimiter))

# def converter(string, delimiter):
    # res = {}
    # temp_list = string.split(delimiter)
    # for i in temp_list:
    #     res[i] = temp_list.count(i)
    # return res

def converter(string, delimiter):
    temp_list = string.split(delimiter)
    res_dict = dict.fromkeys(temp_list)


my_str = 'football, ball, foot, football'
delim = ', '
print(converter(my_str, delim))
