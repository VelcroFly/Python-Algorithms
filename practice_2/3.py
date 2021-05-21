"""Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486, надо вывести
6843"""


def reverse_number(n):
    if n < 10:
        return n
    else:
        return int(str(n % 10) + str(reverse_number(n // 10)))


def reverse_number_v2(n):
    return ''.join([i for i in str(n)[::-1]])


if __name__ == '__main__':
    print(reverse_number(3486))
    number = int(input('Введите число: '))
    print(reverse_number(number))
    print(reverse_number_v2(number))
