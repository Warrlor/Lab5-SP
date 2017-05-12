import sys
n = int(input('Введите кол-во строк матрицы - '))
m = int(input('Введите кол-во столбцов матрицы - '))
a = []
min_count = sys.maxsize + 1
min_column = 0
count = 0

for i in range(n):
    row = input().split()
    for i in range(m):
         row[i] = int(row[i])
    a.append(row)

for i in range(m):
    for j in range(n):
        index_sum = i+j
        if (index_sum != 0):
            if ((a[j][i] >= index_sum) and (a[j][i] % index_sum == 0)):
                count = count + 1
    if (count < min_count):
        min_count = count
        min_column = i
    count = 0

print('Искомый столбец - ', min_column)
