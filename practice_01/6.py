# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

user_input = int(input('Введите порядковый номер буквы(1-26): '))
user_input = ord('a') + user_input - 1
print(f'Это символ {chr(user_input)}')
