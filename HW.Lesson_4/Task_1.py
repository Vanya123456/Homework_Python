import sys

if 'h' in sys.argv:
    print('Введите через пробел три параметра: Выработку часов, ставку в час и премию сотрудника')
else:
    first_param, second_param, third_param = sys.argv[1:]
    wage = float(first_param) * float(second_param) + float(third_param)
    print(f'Заработная плата сотрудника равна: {round(wage, 2)}')
