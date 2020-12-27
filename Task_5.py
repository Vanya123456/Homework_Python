proceeds = int(input("Введите сумму выручки"))
costs = int(input("Введите сумму издержек"))
difference = proceeds - costs
if difference > 0:
    print("Фирма отработала с прибылью: " + str(difference))
    print("Рентабельность: " + "%.2f" % ((difference / proceeds) * 100) + "%")
    profitability_of_employees = difference / int(input("Введите количество сотрудников"))
    print("Прибыль на одного сотрудника составляет: " + "%.2f" % (profitability_of_employees / 1))
elif difference < 0:
    print("Фирма отработала в убыток: " + str(difference))
else:
    print("Фирма отработала в ноль")


