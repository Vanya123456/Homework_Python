with open('Task_3_Test.txt', encoding='utf-8') as f_obj:
    average_salary = 0
    for line in f_obj.readlines():
        content = line.split()
        for i in content:
            try:
                salary = float(i)
                average_salary += salary
                if salary < 20000:
                    print(f'{content[0]}: {content[1]}')
            except ValueError:
                continue
    print(f'Средний оклад сотрудников: {round(average_salary/11, 2)}')
