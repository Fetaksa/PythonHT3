# Задача 1.
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

my_list = []
n = int(input('Задайте количество элементов в массиве: '))
for i in range(n):
    element = int(input('Введите целое число: '))
    my_list.append(element)
print(my_list)
x = int(input('Введите число X: '))
print(my_list.count(x))