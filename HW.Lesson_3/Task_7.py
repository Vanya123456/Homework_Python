def my_func():
    user_word = input('Введите слова маленькими латинскими буквами!').split()
    for i in user_word:
        print(i.capitalize(), end=' ')


my_func()
