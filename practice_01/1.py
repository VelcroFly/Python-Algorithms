# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
user_input = int(input('Введите трехзначное число: '))

hundreds = user_input // 100
dozens = user_input % 100 // 10
units = user_input % 10

summary = hundreds + dozens + units
multiplication = hundreds * dozens * units

print(f'Результат суммирования: {summary}')
print(f'Результат перемножения: {multiplication}')
