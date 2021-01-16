def my_func(x, y):
    try:
        x, y = int(x), int(y)
        result= x / y
    except ZeroDivisionError:
        print("На 0 делить нельзя!")
    print(result)


my_func(x, y)
