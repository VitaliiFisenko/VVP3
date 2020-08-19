# Морской
# бой
import random


class XO:
    def __init__(self):
        self.table = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ]
        self.table_map = {
            '1': [0, 0],
            '2': [0, 1],
            '3': [0, -1],
            '4': [1, 0],
            '5': [1, 1],
            '6': [1, -1],
            '7': [-1, 0],
            '8': [-1, 1],
            '9': [-1, -1],
        }

    def make_mark(self, field_num, sign):
        coords = self.table_map[field_num]
        self.table[coords[0]][coords[-1]] = sign

    def __str__(self):
        return f"{self.table[0][0]}\t | {self.table[0][1]}\t | {self.table[0][-1]}\n" \
               f"{self.table[1][0]}\t | {self.table[1][1]}\t | {self.table[1][-1]}\n" \
               f"{self.table[-1][0]}\t | {self.table[-1][1]}\t | {self.table[-1][-1]}\n"


# def main():
#     xo = XO()
#     print(xo)
#     while True:
#         field_num = input('field_num')
#         sign = input('sign')
#         xo.make_mark(field_num, sign)
#         print(xo)
#
#
# if __name__ == '__main__':
#     main()

class Ship:
    def __init__(self, number):
        self.floors = number

    def __repr__(self):
        return str(self.floors)


class A:
    a = {'a': 1}


class B(A):

    def change_a(self):
        super().a = 1


class C(A):
    pass


# b = B()
#
# n = A()

# print(b.a)
# print(n.a)
# b.change_a()
# print(b.a)
# print(n.a)
#
# m = C()
#
# print(m.a, 'C')
# print(n.a)

_A__attr = 3


class A:
    def get_attr(self):
        return __attr



attr = type('ABC', (), {'b': 5})

print(attr)
print(attr.b)
