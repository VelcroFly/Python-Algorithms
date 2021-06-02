import timeit
import cProfile
"""Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».

Второй — без использования «Решета Эратосфена»."""


def sieve(n):
    size = n ** 2 + n * 2
    a = [0] * size
    for i in range(size):
        a[i] = i

    a[1] = 0
    m = 2

    while m < size:
        if a[m] != 0:
            j = m ** 2
            while j < size:
                a[j] = 0
                j += m
        m += 1

    pos = 0
    for i in a:
        if a[i] != 0:
            pos += 1
            if pos == n:
                return a[i]


def prime(n):
    counter = 1
    current_prime = 2
    while counter < n:
        current_prime += 1
        for i in range(2, current_prime):
            if current_prime % i == 0:
                break
        else:
            counter += 1
    return current_prime


if __name__ == '__main__':
    # print(prime(4))
    # print(prime(1))
    # print(sieve(2))
    # print(sieve(5))
    # print(sieve(4))
    # print(sieve(1))
    # cProfile.run('sieve(3000)')
    # 4 function calls in 3.394 seconds
    #
    # Ordered by: standard name
    #
    # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    # 1    3.334    3.334    3.334    3.334 2.py:12(sieve)
    # 1    0.060    0.060    3.394    3.394 <string>:1(<module>)
    # 1    0.000    0.000    3.394    3.394 {built-in method builtins.exec}
    # 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    # cProfile.run('prime(3000)')
    # 4 function calls in 2.064 seconds
    #
    # Ordered by: standard name
    #
    # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    # 1    2.064    2.064    2.064    2.064 2.py:37(prime)
    # 1    0.000    0.000    2.064    2.064 <string>:1(<module>)
    # 1    0.000    0.000    2.064    2.064 {built-in method builtins.exec}
    # 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    n = 2
    while n < 1025:
        n *= 2
        # print(n, timeit.timeit('sieve(n)', number=1000, globals=globals()))
        # 4 0.005490200000000001
        # 8 0.017000799999999996
        # 16 0.0631929
        # 32 0.3187641
        # 64 1.0874768
        # 128 4.3245893
        # 256 18.9613311
        # 512 82.9405242
        # 1024 350.81500330000006
        print(n, timeit.timeit('prime(n)', number=1000, globals=globals()))
        # 4 - 0.0019303000000000028
        # 8 - 0.008154500000000002
        # 16 - 0.030771
        # 32 - 0.10533369999999999
        # 64 - 0.4099511
        # 128 - 1.9906184000000002
        # 256 - 9.4010818
        # 512 - 45.961447400000004
        # 1024 - 209.6232454
