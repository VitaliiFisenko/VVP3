class Person:
    def __init__(self, mame, age):
        self.name = mame
        self.age = age
        self.__friends = []

    def know(self, other_person):
        if other_person in self.__friends:
            return
        self.__friends.append(other_person)
        other_person.know(self)

    def is_known(self, other_person):
        if other_person in self.__friends:
            return True
        return False


# p1 = Person('111', 12)
# p2 = Person('222', 22)
#
# p1.know(p2)
#
# print(p2.is_known(p1))

class Figure:
    def __init__(self, side_1):
        self.side_1 = side_1

    def perimeter(self):
        raise NotImplementedError

    def square(self):
        raise NotImplementedError


class Triangle(Figure):
    def __init__(self, side_1, side_2, side_3):
        self._validate_figure(side_1, side_2, side_3)
        super().__init__(side_1)
        self.side_2 = side_2
        self.side_3 = side_3

    def _validate_figure(self, side_1, side_2, side_3):
        # какая-то логика по валидации
        if side_1 <= 0:
            raise ValueError
        elif side_2 <= 0:
            raise ValueError

    def perimeter(self):
        pass

    def square(self):
        pass


class PropertyError:
    def __init__(self):
        self._a = 'a'

    @property
    def a(self):
        return self.a

    @a.setter
    def a(self, val):
        self._a = val

#
# b = PropertyError()
