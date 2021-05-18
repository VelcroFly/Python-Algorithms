"""Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел. Количество вводимых чисел и цифра, которую
необходимо посчитать, задаются вводом с клавиатуры."""


def count_numbers(a, b):
    if a // b == 0:
        if a == b:
            return 1
        else:
            return 0
    if a % 10 == b:
        return 1 + count_numbers(a // 10, b)
    else:
        return count_numbers(a // 10, b)


if __name__ == '__main__':
    print(count_numbers(1121345, 1))
    print(count_numbers(331212, 2))
    sequence = int(input('Введите последовательность чисел: '))
    find_value = int(input('Введите искомое число: '))
    print(f'Число {find_value} в последовательности {sequence} встретилось {count_numbers(sequence, find_value)} раз')
