a = []
sum = 0
mult = 1
for i in range (0, 14):
    a.append(int(input()))
    if (i % 2 == 0):
        sum = sum + a[i]
    if (a[i] % 2 == 1):
        mult = mult * a[i]
print('Сумма четных по индексу элементов: ', sum)
print('Произведение нечётных по значению элементов: ', mult)
