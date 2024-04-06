import numpy as np

# Определение узлов и соответствующих значений функции
x = np.array([-1, 0, 1])
y = x ** 2


def lagrange(x, y, xp):
    yp = 0
    for i in range(len(y)):
        p = 1
        for j in range(len(x)):
            if i != j:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += y[i] * p
    return yp


# Примеры точек для демонстрации
x_points = np.linspace(-1, 1, 5)  # Генерация 5 точек между -1 и 1 для демонстрации

# Вычисление и вывод результатов
for xp in x_points:
    yp = lagrange(x, y, xp)
    print(f"Значение интерполяционного полинома Лагранжа в точке x = {xp} равно {yp}")
