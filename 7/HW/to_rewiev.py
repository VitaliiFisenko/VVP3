"""
Написать игру. 2 игрока бросают игровые кубики по 10 раз,

нужно определить кто выиграл и вывести результаты обоих игроков (суммы бросков).

Если у двух игроков за 1 ход выпало на кубиках одинаковое число, то игроки перебрасывают кубики.
"""

"""
Посмотреть, подебажить код. Он написан императивно(((Нужно убрать лишний код, выделить отдельные части,
вынести их в функции и заускать через if __name__ == ...
"""

import random

y_n = 'yes'
while y_n == 'yes':
    random_number = random.randint(1, 1000)
    for i in range(10):
        print(f'У вас {10 - i} попыток!')
        try:
            player_select = int(input('Введите число:'))
        except ValueError as err:
            print('Error you number not correct!')
            y_n = 'error'
            break
        if player_select == random_number:
            print('You win!!!!')
            y_n = input('Хотите прожолжить?[yes/no]')
            break
        elif player_select > random_number:
            print('Вваше число больше')
        elif player_select < random_number:
            print('Вваше число Меньше')
