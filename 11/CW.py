# file = open('file.txt')
# file.close()
#
# with open('file.txt') as file1:
#     print(file1.read())

A = 10


def add(a, b):
    return a + b


class Person:
    _eyes_count = 2

    def __init__(self, name, last_name, gender='male'):
        self.name = name
        self.last_name = last_name
        self.__genders = [gender]
        self.eyes_count = self._eyes_count

    @property
    def gender(self):
        return self.__genders[-1]

    @gender.setter
    def gender(self, value):
        self.__genders.append(value)

    @gender.deleter
    def gender(self):
        self.__genders.pop()

    def say_hay(self):
        print(self.eyes_count)
        print(self.static(2, 5))

    @classmethod
    def add_eyes(cls, count):
        cls._eyes_count += count

    @classmethod
    def create_person(cls, name, last_name, gender='male'):
        return cls(name, last_name, gender)

    @staticmethod
    def static(value1, value2):
        print('I"m static')
        return value1 ** value2


pers1 = Person('Ivan', 'Ivanov')
pers2 = Person('Iv', 'Iv')
pers3 = Person.create_person('aa', 'jkbfnv', gender='ghjk')

Person.add_eyes(3)
pers1.add_eyes(4)
print(Person._eyes_count)
Person.static(1, 2)
pers2.static(1, 4)
pers2.say_hay()
print(pers3.gender)
# print(pers1.gender)
#
# pers1.gender = 'female'
#
# print(pers1.gender)
# del pers1.gender
