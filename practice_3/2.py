"""Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа."""

import random


def fn(values_list):
    result = []

    for pos, item in enumerate(values_list):
        if item % 2 == 0:
            result.append(pos)
    return result


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


if __name__ == '__main__':
    print(f'Сгенерированный массив: {array}')
    print(f'Индексы четных элементов: {fn(array)}')
