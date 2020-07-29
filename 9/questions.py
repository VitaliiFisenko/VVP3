import string


def converter(date, format_from, forat_to):
    pass


my_date = ''
time_forat = ''
converter(my_date, time_forat, '')


# def parse(rules):
#     res = []
#     value = 0
#     for rule in rules:
#         if rule == 'i':
#             value += 1
#         elif rule == 's':
#             value *= value
#         elif rule == 'd':
#             value -= 1
#         elif rule == 'o':
#             res.append(value)
#     return res

def parse(rules):
    res = []
    value = 0

    def inc(value):
        return value + 1

    def dec(value):
        return value - 1

    def sq(value):
        return value * value

    rule_dict = {
        'i': inc,
        'd': dec,
        's': sq,
    }
    for rule in rules:
        if rule == 'o':
            res.append(value)
            continue
        try:
            value = rule_dict[rule](value)
        except KeyError:
            print('warn')

    return res


#
# print(parse("iiisdoso"))

# slice

l = list(range(0, 101))
t = tuple(l)
s = 'jksdncjknsdknckjnesrncjl'

print(t[-1])
print(t[0])
print(t[:-1])
print(t[::-1])

