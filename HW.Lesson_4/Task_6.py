from itertools import count, cycle

my_list = []
for el in count(1):
    if el > 10:
        break
    else:
        my_list.append(el)

c = 0
for el in cycle(my_list):
    if c > 19:
        break
    else:
        print(el)
        c += 1
