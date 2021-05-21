"""Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2,
где n — любое натуральное число."""


def count_sum(n):
    if n == 1:
        return n
    res = n + count_sum(n-1)
    return res


n = int(input('Введите любое натуральное число'))
left = count_sum(n)
right = n * (n + 1)/2
if left == right:
    print('Верно')
else:
    print('Неверно')
