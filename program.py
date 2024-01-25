take = []
give = []
i = 0
count = int(input('Введите кол-во элементов: '))
while i < count:
    take.append(input('Введите элемент: '))
    if len(take[i]) <= 3:
        give.append(take[i])
    i += 1
print(take) #Эта строка необязательна.
print(give)