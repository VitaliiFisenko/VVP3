class Car:
    def __init__(self, color, wheels, brand):
        self.color = color
        self.wheels = wheels
        self.brand = brand

    def ride(self):
        return 'ok'


# car2 = Car('red', 10, 'aaaa')

# car = Car('зеленый', 4, 'ford')

# print(car)
# print(car.color)
# print(car.wheels)
# print(car.brand)
# print(car.ride())
# print('*' * 10)
# print(car2)
# print(car2.color)
# print(car2.wheels)
# print(car2.brand)


#  Инкапсуляция


class SomeClass:
    def __init__(self, self_name):
        self._name = self_name

    def _say_name(self):
        return self._name + '\n'

    def say_name(self):
        return self._say_name()


# inst = SomeClass('Ololo')
#
#
# print(inst.say_name())
class ParentParert:
    def __init__(self):
        print('kjnsdjc')


class BaseCar:
    def __init__(self, color, wheels, brand):
        self.color = color
        self.wheels = wheels
        self.brand = brand

    def ride(self):
        return 'ok'


class TrackMixin:
    def __init__(self, color, wheels, brand, trailer):
        super().__init__(color, wheels, brand)
        self.trailer = trailer


class Track(TrackMixin, BaseCar):
    def ride(self):
        return 'Nope'


track = Track('red', 10, 'aaaa', True)

print(Track.__mro__)
print(track.trailer)
print(track.ride())
import requests
import base64


class Ticket:
    def __init__(self, info, qr):
        self.info = info
        self.__qr = qr

    def trim_qr(self):
        return ''

    def get_qr(self):
        qr = self.trim_qr()
        return qr


class QrReader:
    def __init__(self, url):
        self.url = url

    def precess_qr(self, ticket):
        data = {
            'qr_code': ticket.get_qr()
        }
        resp = requests.post(self.url, data=data)
        if resp.status_code == 200:
            return resp.json()['result']


def read_file(file):
    info, qr = '', ''
    return info, qr


# def main():
#     with open('ticket.jpeg', 'b') as file:
#         ticket = Ticket(*read_file(file))
#         reader = QrReader('http://localhost')
#         benefits = reader.precess_qr(ticket)
#         print(benefits)

def precess_qr(url, qr):
    data = {
        'qr_code': qr
    }
    resp = requests.post(url, data=data)
    if resp.status_code == 200:
        return resp.json()['result']


def prepare_qr(qr):
    return qr


def main():
    with open('ticket.jpeg', 'b') as file:
        info, qr = read_file(file)
        reader = 'http://localhost'
        benefits = precess_qr('http://localhost', prepare_qr(qr))
        print(benefits)


if __name__ == '__main__':
    main()
