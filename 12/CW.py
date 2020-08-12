from dataclasses import dataclass


class CustomInt(int):
    def __add__(self, other):
        if isinstance(other, str):
            other = len(other)
        return super().__add__(other)

    # def __call__(self, *args, **kwargs):
    #     print('I"m callable')


# a = CustomInt(8)
# print(a)
# print(type(a))
# b = a + '12345'
# print(a)

class Person:
    def __init__(self):
        self.name = 'Ivan'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{self.__class__} {self.__module__} {self.name}'


class ListObjectDict(dict):
    def __iter__(self):
        return self.values().__iter__()

    def __getitem__(self, key):
        if isinstance(key, int):
            return list(self.values())[key]
        try:
            return super().__getitem__(key)
        except KeyError:
            raise KeyError

    def pop(self, key, *args):
        try:
            return super().pop(key, *args)
        except KeyError:
            raise KeyError

    def get(self, key, default=None):
        return super().get(key, default)

    def append(self, obj):
        self[obj['id']] = obj


from collections import namedtuple

my_tuple = namedtuple('my_tuple', ['a', 'b'])
t = my_tuple(1,2)
# print(t.a)
# print(t.b)


@dataclass
class Point:
    x: float
    y: float
    z: float

    def summm(self):
        return self.x + self.z + self.y
