"""В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""


def fn(start_value, end_value, start_divider, end_divider):

    division_counter = [0] * (end_divider - start_divider + 1)
    for i in range(start_value, end_value + 1):
        for j in range(start_divider, end_divider + 1):
            if i % j == 0:
                division_counter[j - start_divider] += 1
    return division_counter


if __name__ == '__main__':
    print(fn(start_value=2, end_value=99, start_divider=2, end_divider=9))
