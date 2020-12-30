def user_data(**kwargs):
    for key, val in kwargs.items():
        print(str(key) + ' : ' + str(val), end=', ')


print(user_data(name=input('Имя: '),
                surname=input('Фамилия: '),
                year_of_birth=input('Год рождения: '),
                city=input('Город проживания: '),
                email=input('Электронный адрес: '),
                tel=input('Мобильный телефон: ')
 ))


user_data()