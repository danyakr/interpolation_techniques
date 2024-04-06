import math


def lagrange(x, y, arg_x):
    d = []  # Сохранение промежуточных вычислений разностей

    # Вычисляем разности
    for i in range(len(x)):
        diff = 1
        for j in range(len(x)):
            if i != j:
                diff *= (arg_x - x[j]) / (x[i] - x[j])
        d.append(diff)

    # Вычисляем значения многочлена Лагранжа в точке
    result = sum([y[i] * d[i] for i in range(len(x))])

    return round(result, 6)


# Определение узлов и соответствующих значений функции
x = [0, 1/6, 1/2]
y = [math.sin(math.pi * xi) for xi in x]
arg_x = [1/4, 1/3]

for xi in arg_x:
    yp = lagrange(x, y, xi)
    print(f"Значение интерполяционного полинома Лагранжа в точке x = {xi} равно {yp:.5f}")