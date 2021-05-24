"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""
import random


def find_max_negative(values_list):
    pos = 0
    max_negative = float('-inf')

    for i in range(len(values_list)):
        if values_list[i] < 0:
            if max_negative < values_list[i]:
                pos = i
                max_negative = values_list[i]
    return pos, max_negative


if __name__ == '__main__':
    SIZE = 10
    MIN_ITEM = -100
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(f'Сгенерированный массив: {array}')
    print(find_max_negative(array))
    print(f"""Максимальное отрицательное значение = {find_max_negative(array)[1]},
находится под индексом {find_max_negative(array)[0]}""")
