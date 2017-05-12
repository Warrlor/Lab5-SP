n = 4
m = 5
a = []
mid = 0
count = 0
for i in range(n):
    row = input().split()
    for i in range(m):
         row[i] = int(row[i])
         mid = mid + row[i]
    a.append(row)

mid = mid / (n * m)

for i in range(n):
    for j in range(m):
        if (a[i][j] > mid):
            count = count + 1
print('Среднее арифметическое - ', mid)
print('Кол-во элементов, больших среднего арифметического - ', count)
