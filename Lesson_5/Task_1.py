f = open('Test.txt', 'w+')
while True:
    user_answer = input('Введите свои личные данные в формате "Имя - Enter, Фамилия - Enter и т.д)".'
                        'Для выхода нажмите Enter.')
    f.write(user_answer + '\n')
    if not user_answer:
        break
f.seek(0)
print(f.read())
f.close()
