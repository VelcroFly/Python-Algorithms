from collections import deque
"""Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""


def hex_sum(n1, n2):
    hex_base = 16
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', ]
    dec_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                }
    result = deque()
    n1 = deque(n1)
    n2 = deque(n2)

    if len(n1) < len(n2):
        n1, n2 = n2, n1
    n2.extendleft('0' * (len(n1) - len(n2)))

    rest = 0
    while n1:
        term_1 = dec_dict[n1.pop()]
        term_2 = dec_dict[n2.pop()]
        res_sum = term_1 + term_2 + rest

        if res_sum > hex_base:
            rest = 1
            res_sum -= hex_base
        else:
            rest = 0

        result.appendleft(hex_list[res_sum])

    if rest == 1:
        result.appendleft('1')
    return ''.join(result)


if __name__ == '__main__':
    num_1 = input('Введите первое шестнадцатеричное число: ').upper()
    num_2 = input('Введите второе шестнадцатеричное число: ').upper()
    print(f'{num_1} + {num_2} = {hex_sum(num_1, num_2)}')
