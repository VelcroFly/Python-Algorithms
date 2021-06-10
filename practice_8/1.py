"""Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9"""

import hashlib


def count_distinct_substring(string):
    result = set()

    for i in range(len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            if hashlib.sha1(string[i:j].encode('utf-8')).hexdigest() !=\
                    hashlib.sha1(string.encode('utf-8')).hexdigest():
                result.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
    return len(result)


if __name__ == '__main__':
    print(count_distinct_substring("papa"))
    print(count_distinct_substring("sova"))
