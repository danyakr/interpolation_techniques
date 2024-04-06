
arg_x = 0.1157  # Значение аргумента
# Узлы и значения функции
x = [0.101, 0.106, 0.111, 0.116, 0.121, 0.126]
y = [1.26183, 1.27644, 1.29122, 1.30617, 1.32130, 1.32660]
d = []
diffs = [[], [], [], [], [], []]



# Вычисляем разности и перемножаем их
for i in range(len(x)):
    mult = 1
    for j in range(len(x)):
        if i != j:
            difference = x[i] - x[j]
            mult *= difference
            diffs[i].append(round(difference, 6))
    diffs[i].insert(i, round(arg_x - x[i], 6))
    d.append(mult * (arg_x - x[i]))

# Суммируем частные
sum = 0
for i in range(len(x)):
    sum += y[i]/d[i]

p = 1
for i in range(len(x)):
    p *= arg_x - x[i]

print(round(p*sum, 6))


# Функции для вывода таблицы
def print_table_header():
    # Заголовки столбцов
    header = f"{'i':^5} {'differences':^50} {'di':^10} {'yi/di':^20}"
    # Разделительная линия
    separator = "-" * len(header)

    print(header)
    print(separator)


def print_table_row(i, di, yi_di, differences):
    # Форматирование строки таблицы
    str_differences = ', '.join([str(i) for i in differences])
    table_row = f"{i:^5} {str_differences:^50} {di:^10} {yi_di:^20}"
    print(table_row)


print_table_header()
for i in range(len(x)):
    print_table_row(i, round(d[i], 13), round(y[i]/d[i], 1),  diffs[i])
