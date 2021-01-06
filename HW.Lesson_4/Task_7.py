def fact(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    yield factorial

for el in fact(5):
    print('Факториал вашего числа равен: ' + str(el))
