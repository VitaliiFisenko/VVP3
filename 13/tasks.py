"""
Реализовать класс цифрового счетчика. Обеспечьте возможность установки максимального и минимального значений,
увеличения счетчика на 1, возвращения текущего значения.
"""


class DigitalCounter:
    def __init__(self):
        self.counter = 9998
        self.max_value = 9999

    def increment_counter(self):
        predicted = self.counter + 1
        if predicted > self.max_value:
            raise ValueError('kjndskjc')
        self.counter += 1


# c = DigitalCounter()
#
# c.increment_counter()


"""
Создать класс воина, создать 2 или больше объектов воина с соответствующими воину атрибутами. Реализовать методы,
которые позволять добавить силы воину, улучшить оружие. Реализовать возможность драки 2х воинов с потерей здоровья,
приобретения опыта.
"""


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Warrior:
    def __init__(self, name, power, hp, arm):
        self.name = name
        self.power = power
        self.hp = hp
        self.arm = arm
        self.weapons = {'first': Weapon("Fist", 1)}
        self.weapon = self.weapons['first']
        self.exp = 0

    def change_weapon(self, name):
        self.weapon = self.weapons[name]

    def add_weapon(self, name, damage):
        self.weapons.update({name: Weapon(name, damage)})

    def drop_weapon(self, name):
        if name in self.weapons:
            self.weapons.pop(name)
        print('((((((((')

    def bit_other(self, other_warior):
        if other_warior.arm == 0:
            other_warior.hp -= self.weapon.damage
        elif self.weapon.damage > other_warior.arm:
            diff = self.weapon.damage - other_warior.arm
            other_warior.hp -= diff
        else:
            other_warior.arm -= self.weapon.damage
        self.exp += (other_warior.hp * self.weapon.damage) / 100

    def bid_self(self):
        self.hp -= self.weapon.damage


samuray = Warrior('samuray', 122, 100, 0)
samuray2 = Warrior('samuray2', 122, 100, 10)

print(samuray.hp)
print(samuray2.hp)
samuray.bit_other(samuray2)
print(samuray2.hp)
print(samuray2.arm)
samuray.bit_other(samuray2)
samuray.bit_other(samuray2)
samuray.bit_other(samuray2)
samuray.bit_other(samuray2)
samuray.bit_other(samuray2)
samuray.bit_other(samuray2)
samuray.bit_other(samuray2)
samuray.bit_other(samuray2)
samuray.bit_other(samuray2)
samuray.bit_other(samuray2)
samuray.bit_other(samuray2)
samuray.bit_other(samuray2)
print(samuray2.hp)
print(samuray2.arm)
