def my_func(a, b, c):
    result_1 = a + b
    result_2 = b + c
    result_3 = a + c
    return max(result_1, result_2, result_3)


print(my_func(3, 4, 5))