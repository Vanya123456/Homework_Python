my_list = [7, 5, 3, 3, 2]
for i in my_list:
    user_answer = input('Введите любое число для добавления в рейтинг. Для выхода нажмите \"q\"')
    if user_answer == '0':
        print('Введите число больше 0!')
    elif user_answer == 'q':
        break
    else:
        my_list.append(int(user_answer))
        my_list_2 = sorted(my_list)
        my_list_2.reverse()
        print(my_list_2)
