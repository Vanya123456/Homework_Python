with open('Task_5_Test.txt', 'w+') as f:
    user_numbers = input('Введите числа через пробел. После окончания нажмите Enter.')
    f.write(user_numbers)
    f.seek(0)
    the_sum = 0
    for el in user_numbers.split():
        the_sum += int(el)
    print(f'Сумма введенных вами чисел равна: {the_sum}. Числа сохранены в файл.')
