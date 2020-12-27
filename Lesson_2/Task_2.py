user_list = list(input('Напишите что-то'))
user_length_list = len(user_list)
for i in range(1, user_length_list, 2):
    user_list[i - 1], user_list[i] = user_list[i], user_list[i - 1]
print(user_list)
