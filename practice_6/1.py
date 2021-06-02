"""Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа."""
import sys

# Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
result = []
memory_taken = 0

values_list = list(input('Введите числовую последовательность. Например, 1234567: '))
memory_taken += sys.getsizeof(values_list)

for pos, item in enumerate(values_list):
    if int(item) % 2 == 0:
        result.append(pos)

print(result)

memory_taken += sys.getsizeof(result)
print(memory_taken)
# Затраты: 200 байт

print('*' * 20)

memory_taken = 0
values_list = list()
elements_counter = int(input('Введите кол-во элементов массива: '))
memory_taken += sys.getsizeof(elements_counter)

while elements_counter != 0:
    values_list.append(int(input('Введите элемент: ')))
    elements_counter -= 1

result = [pos for pos, i in enumerate(values_list) if i % 2 == 0]
print(result)

memory_taken += sys.getsizeof(result)
print(memory_taken)
# Затраты: 116 байт. Затраты памяти меньше в связи с тем, что values_list наполняется целочисленными значениями
