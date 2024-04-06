import matplotlib.pyplot as plt


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

    return result


# Определение узлов и соответствующих значений функции
x = [-1, 0, 1]
y = [xi**2 for xi in x]

# Входные данные для построения графика
arg_x = [i/10 for i in range(-30, 31)]  # Генерация значений от -3 до 3
arg_y = [lagrange(x, y, val) for val in arg_x]

# Построение графика
plt.plot(arg_x, arg_y, label='Lagrange Interpolation')
plt.scatter(x, y, color='red', label='Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation Polynomial')
plt.legend()
plt.grid(True)
plt.show()
