# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


N = int(input('введите размер массива'))
myList = [0]*N


for i in range(len(myList)):
    myList[i] = i


x = int(input('Введите число, которое хотите найти в массиве'))

count = 0

for i in range(len(myList)):
    if i == x:
        count = count +1
    
print(f'{x} встречалась в массиве {count} раз')
    
