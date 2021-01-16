def my_func():
    exit = False
    result = 0
    while exit == False:
        numbers = input('Введите числа. Для выхода из программы нажмите "q" ').split()
        result_2 = 0
        for i in numbers:
            if 'q' in i:
                exit = True
                break
            result_2 += int(i)
        result += result_2
    print(result)


my_func()