user_string = input('Введите какую-нибкь фразу')
words = user_string.split()
for i, el in enumerate(words, 1):
    print(i, el[: 10])
