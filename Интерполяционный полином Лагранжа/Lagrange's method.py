
arg_x = 0.263  # Значение аргумента
# Узлы и значения функции
x = [0.05, 0.10, 0.17, 0.25, 0.30, 0.36]
y = [0.050042, 0.100335, 0.171657, 0.255342, 0.309336, 0.376403]
d = []
diffs = [[], [], [], [], [], []]

# Вычисляем разности и перемножаем их
for i in range(len(x)):
    mult = 1
    for j in range(len(x)):
        if i != j:
            difference = x[i] - x[j]
            mult *= difference
            diffs[i].append(difference)
    diffs[i].insert(i, arg_x - x[i])
    d.append(round(mult * (arg_x - x[i]), 11))

# Суммируем частные
sum = 0
for i in range(len(x)):
    sum += y[i]/d[i]

p = 1
for i in range(len(x)):
    p *= arg_x - x[i]

print(round(p*sum, 6))
print(diffs)
