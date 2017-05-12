x = []
y = []
denom = 1
numer = 1
for i in range (0, 10):
    x.append(int(input()))
    y.append(x[i] * x[i] + 0.3)
    if (i % 2 == 0):
        denom = denom * x[i] * y[i]
    else:
        numer = numer * x[i] * y[i]

if (denom == 0):
    print('деление на 0')
else:
    rest = numer % denom
    p = numer / denom + rest
    print('Массив Х: ', x)
    print('Массив Y: ', y)
    print('Сумма P: ', p)
    print('Остаток: ', rest)
