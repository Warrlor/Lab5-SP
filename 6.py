import sys
a = []
n = 5
m = 5

for i in range(n):
    row = [0, 0, 0, 0, 0]
    for i in range(m):
         row[i] = int(row[i])
    a.append(row)

for i in range(n):
    for j in range(m):
        if (i == 2) or (j == 2):
            a[i][j] = 1
        else:
            a[i][j] = 0

for i in range(n):
    for j in range(m):
        sys.stdout.write("%d" % (a[i][j]))
    print()
