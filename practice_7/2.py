"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""
import random


def merge_sort(arr):
    result = list()
    if len(arr) < 2:
        return arr

    divider = int(len(arr) / 2)
    left = merge_sort(arr[:divider])
    right = merge_sort(arr[divider:])

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    result += left[i:]
    result += right[j:]
    return result


if __name__ == '__main__':
    array = [i for i in range(50)]
    random.shuffle(array)
    print(array)
    # print(merge_sort([2, 5, 1, 5, 7, 1, 9]))
    print(merge_sort(array))
