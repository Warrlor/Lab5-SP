import sys 
min = sys.maxsize
max = -sys.maxsize - 1
min_i = 0
max_i = 0

binary_array = []
tmp_binary = 0 
count = int(input('Введите кол-во чисел'))

for i in range(0,count):

    tmp_binary = int(input())
    binary_array.append(tmp_binary)
    
    
    if (binary_array[i] > max):
        max = binary_array[i]
        max_i = i
    if (binary_array[i] < min):
        min = binary_array[i]
        min_i = i

if (abs(max_i - min_i) > 1):
    print('Между минимальным и максимальным значением находится ', abs(max_i - min_i) - 1, ' элементов')
else:
    print('Между минимальным и максимальным значениями нет элементов')
