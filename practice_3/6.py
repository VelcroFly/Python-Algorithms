"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""
import random


def find_min_max_indexes(values_list):
    index_min = 0
    index_max = 0
    for i in range(len(values_list)):
        if values_list[i] < values_list[index_min]:
            index_min = i
        if values_list[i] > values_list[index_max]:
            index_max = i

    if index_min > index_max:
        index_min, index_max = index_max, index_min
    return index_min, index_max


def count_sum(start_index, end_index, values_list):
    result = 0
    for i in range(start_index + 1, end_index):
        result += values_list[i]
    return result


if __name__ == '__main__':
    SIZE = 10
    MIN_ITEM = -100
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(f'Сгенерированный массив: {array}')
    print(f'Min/max индексы: {find_min_max_indexes(array)}')
    print(f'Сумма элементов: {count_sum(find_min_max_indexes(array)[0], find_min_max_indexes(array)[1], array)}')
