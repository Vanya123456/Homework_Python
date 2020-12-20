user_seconds = int(input("Введите число секунд для преобразования"))
hours = str(user_seconds//3600)
mins = str((user_seconds%3600)//60)
seconds = str((user_seconds%3600)%60)
time = [f"{hours} часов {mins} минут {seconds} секунд"]
print(time)
