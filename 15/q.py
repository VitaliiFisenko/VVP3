class Person:
    def __init__(self, name):
        self.name = name
        self.q = 0

    def __str__(self):
        if self.q:
            return f'{self.name}ич'
        return self.name


# p = Person('Ivan')
#
# print_str = p.name if p.q else f'{p.name}ич'
# print(print_str)
class Citizen:
    def __init__(self):
        self.name = 1


class City:
    citizens = []

    def __init__(self):
        self.name = 'll'
        self.population = 111


c1 = City()
cit = Citizen()
c2 = City()
c1.citizens.append(cit)
print(c2.citizens)
print(c1.citizens)