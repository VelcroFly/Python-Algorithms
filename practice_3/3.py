"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random


def swap_min_with_max(values_list):
    min_index = 0
    min_value = values_list[0]
    max_index = 0
    max_value = values_list[0]

    for pos, value in enumerate(values_list):
        if min_value < values_list[pos]:
            min_value = values_list[pos]
            max_index = pos
        if max_value > values_list[pos]:
            max_value = values_list[pos]
            min_index = pos
    values_list[min_index] = min_value
    values_list[max_index] = max_value
    return values_list


if __name__ == '__main__':
    SIZE = 10
    MIN_ITEM = -100
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(f'Сгенерированный массив: {array}')
    print(f'Измененный массив: {swap_min_with_max(array)}')
