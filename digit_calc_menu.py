import calc_func

def digit_calc_menu():
    while 1:
        print('Привет! Это простой калькулятор на языке Python. Какое действие вы хотите выполнить?')
        print('1 - Простые операции')
        print('2 - Расширенные операции')
        print('3 - Тригонометрические действия с градусами')
        print('4 - Тригонометрические действия с радианами')
        print('5 - Логические операции')
        print('6 - Перевод чисел в различные СС')
        print('7 - Проверка скобок')
        print('8 - Выход в главное меню')
        print('0 - Завершение работы')
        choice = int(input('Ваш выбор: '))
        result = 0
        separator = '-----------------------'
        print(separator)
        match choice:
            case 1:
                result = calc_func.calc_simple()
            case 2:
                result = calc_func.calc_extended()
            case 3:
                result = calc_func.calc_degrees()
            case 4:
                result = calc_func.calc_radians()
            case 5:
                result = calc_func.calc_logic()
            case 6:
                result = calc_func.menu_logic()
            case 7:
                result = calc_func.check_brackets()
            case 0:
                print('Спасибо, что воспользовались нашим приложением!')
                break
            case _:
                print('Что-то пошло не по плану, проверьте правильность ввода')
        print()
