with open('lknkcd.txt', 'r') as file, open('lknkcd.txt', 'w') as file_w:
    data = file.read()
    data += 'a'
    file_w.write(data)

#  -------------
"""
Генерация рандомного числа в коде
"""
tries = 10
while tries:

    """
    Ввод и валидация инпута от юзера в функции
    """

    """
    Сравнение рандомного числа и числа юзера отдельная функция, вернет 
    Тру или фолс в зависимости от результата
    """
    if not compare_res(ранд число, юзер число):
        tries -= 1
        continue

    """
    Пишем в файл
    """
    break

