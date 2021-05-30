from collections import namedtuple
"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""
DECADES = 4
decade_dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', }
Enterprise = namedtuple('Enterprises', ['name', 'profit'])
enterprises_list = list()
total_profit = 0

number_of_enterprises = int(input('Ввелите кол-во предприятий: '))

for i in range(number_of_enterprises):
    enterprises_name = input('Ввелите наименование предприятия: ')
    profit = 0

    for j in range(1, DECADES + 1):
        decade_profit = float(input(f'Введите прибыль за {decade_dict[j]} квартал: '))
        profit += decade_profit

    enterprise = Enterprise(name=enterprises_name, profit=profit)
    enterprises_list.append(enterprise)
    total_profit += profit

# for i in enterprises_list:
#     total_profit += i.profit

average_profit = total_profit / number_of_enterprises
print(f'Средняя прибыль: {average_profit}')

lesser_profit = list()
greater_profit = list()

for i in enterprises_list:
    if average_profit > i.profit:
        lesser_profit.append(i.name)
    else:
        greater_profit.append(i.name)

lesser_profit_enterprises = ', '.join(lesser_profit)
greater_profit_enterprises = ', '.join(greater_profit)
print(f'У следующих предприятий прибыль ниже средней прибыли: {lesser_profit_enterprises}')
print(f'У следующих предприятий прибыль ваше средней прибыли: {greater_profit_enterprises}')
