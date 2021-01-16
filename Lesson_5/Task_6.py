with open('Task_6_Test.txt', encoding='utf-8') as f:
    my_dict = {}
    my_list = ['(лаб)', '(л)', '-', '(пр)']
    for line in f.readlines():
        for el in my_list:
            if el in line:
                line = line.replace(el, '')
        my_dict.update({line.split()[0]: sum(map(int, line.split()[1:]))})
print(my_dict)
