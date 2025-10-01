import math


def is_number(s):
    try:
        float(s)
        return True
    
    except ValueError:
        return False
def calc_simple_adv():
    print('Введите выражение, состоящее строго из двух чисел и знака операции. Например: 1+1')
    s = input('Введите ваше выражение: ')

    num1 = 0
    num2 = 0
    count = 0
    is_ready = False
    is_oper = False
    operation = ''

    """ Проверка на число первого элемента """
    if not is_number(s[0]):
        print('Некорректный ввод. Попробуйте снова\n')
        calc_simple_adv()

    for i in s:
        if i != [' ', '+', '-', '/', '*'] and (not is_ready):
            """ Добавление первого числа """
            num1 += i
            
            """ Проверка первого числа """
            if is_number(num1):
                num1 = float(num1)
                is_ready = True
            else:
                print('Некорректный ввод. Попробуйте снова\n')
                calc_simple_adv()
        elif i == [' ', '+', '-', '/', '*'] and is_ready and (not is_oper):
            if i != ' ':
                operation = i
                is_oper = True
        elif i != [' ', '+', '-', '/', '*'] and is_ready:
            """ Добавление второго числа """
            num2 += i
            
            """ Проверка второго числа """
            if is_number(num2):
                num2 = float(num2)
            else:
                print('Некорректный ввод. Попробуйте снова\n')
                calc_simple_adv()
        else:
            print('Что-то пошло не по плану, попробуйте снова\n')
            calc_simple_adv()
    
    if operation == "/" and num2 == 0:
        print('Деление на ноль невозможно, пожалуйста, проверьте ввод')
        calc_simple_adv()
    
    return eval(f"{num1}{operation}{num2}")
          
# Секция в разработке
"""
def calc_extended():
def calc_degrees():
"""

def calc_radians():
    """Задание 4. Тригонометрический калькулятор (Радианы)"""
    """Зависимости: модуль math"""

    while 1:
        operation = input("Введите операцию (sin или cos): ")
        degrees = float(input("Введите угол в радианах: "))

        match operation:
            case 'sin' | 'Sin' | 'SIN':
                return math.sin(degrees)
            case 'cos' | 'Cos' | 'COS':
                return math.cos(degrees)
            case _:
                print('Произошла ошибка, попробуйте снова')
                return
def calc_logic():
    print('Введите действие')
    print('1 - and')
    print('2 - or')
    print('3 - not')
    n= input('Введите числовые значения (1, 2 или 3): ')
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
def menu_logic():
    print('Добро пожаловать в переводчик систем счисления.')
    a = int(input('Основание исходной системы счисления: '))
    b = int(input('Основание конечной системы счисления: '))
    num = int(int(input('Введите исходное число: ')), a)
    match b:
        case 2:
            return bin(num)[2:]
        case 8: 
            return oct(num)[2:]
        case 10: 
            return num
        case 16: 
            return hex(num)[2:]
def check_brackets():
    s = input("Введите строку с формулой: ")
    count = 0

    for i in s:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
        if count < 0 or (count != 0 and i == ['=', '>', '<']):
            return 'НЕТ'
    return 'ДА' if count == 0 else 'НЕТ'
