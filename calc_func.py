import math

def calc_simple():
    """Задание 1. Функция простого калькулятор (+-/*)"""

    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operation = input("Введите операцию : ")

    if operation not in ['+', '-', '/', '*']:
        print("ОШИБКА: Неверно введен оператор")
        return

    if operation == "/" and b == 0:
        print("ОШИБКА: Деление на 0 не допускается")
        return

    res = eval(f"{a}{operation}{b}")
    print(res)

    return res
""" Секция в разработке
def calc_extended():
def calc_degrees():

"""
def calc_radians():
    """Задание 4. Тригонометрический калькулятор (Радианы)"""
    """Зависимости: модуль math"""

    print("1 - sin()\n2 - cos()")
    operation = int(input("Введите номер действия: "))
    degrees = float(input("Введите угол в радианах: "))

    match operation:
        case 1:
            res = math.sin(degrees)
            print(res)
            return res
        case 2:
            res = math.cos(degrees)
            print(res)
            return(res)
        case _:
            print("ОШИБКА: Допускаются исключительно операции 1 и 2")
            return
def calc_logic():
    print('Выберите действие:')
    print('1-and')
    print('2-or')
    print('3-not')
    n= int(input('Введите числовые значения (1, 2 или 3): '))
    c = 0
    if n == 1:
        a=int(input('Введите первое значение (0-False,1-True): '))
        b=int(input('Введите второе значение (0-False,1-True): '))
        с=a and b
        print(f'Результат {a} and {b} = {c} ')
    elif n == 2:
        a=int(input('Введите первое значение (0-False,1-True): '))
        b=int(input('Введите второе значение (0-False,1-True): '))
        с=a or b
        print(f'Результат {a} or {b} = {c} ')
    elif n == 3:
        a=int(input('Введите первое значение (0-False,1-True): '))
        c= not a
        print(f'Результат not {a} = {int(c)}')
    else:
        print('Неправильный ввод: введите 1, 2 или 3')
""" ------ Секция перевода СС ------ """
def calc_10_2():
    n=int(input("Введите число: "))
    binary=bin(n)[2:]
    print(binary)
def calc_10_16():
    n=int(input("Введите число: "))
    hexad=hex(n)[2:]
    print(hexad)
def calc_10_8():
    n=int(input("Введите число: "))
    octal=oct(n)[2:]
    print(octal)
def menu_logic():
    print('1 - Перевод 10СИ->2СИ')
    print('2 - Перевод 10СИ->16CИ')
    print('3 - Перевод 10СИ->8СИ')
    a = int(input())
    if a != 1 and a != 2 and a != 3:
        print('Введите целочисленное число в диапазоне 1>=a>=3')
        menu_logic()
    elif a == 1:
        calc_10_2()
    elif a == 2:
        calc_10_16()
    elif a == 3:
        calc_10_8()
""" ------ Конец  секции перевода СС ------ """
def check_brackets():
    s = input("Введите строку с формулой: ")
    count = 0

    for i in s:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
        if count < 0:
            print("НЕТ")
            return

    print("ДА" if count == 0 else "НЕТ")