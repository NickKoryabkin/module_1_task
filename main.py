import sys


# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
a = 10
b = 1
s = 0
for i in range(a):
    s += b
    b /= -2
# Универсальный код для замера количества памяти, занятой под переменные в произвольной программе
sum_size = 0
sum_size += sys.getsizeof(a)
sum_size += sys.getsizeof(b)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(s)


print('Переменные занимают', sum_size)