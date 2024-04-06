
x = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
y = [0.8427, 0.8802, 0.9103, 0.9340, 0.9523, 0.9661, 0.9763, 0.9838, 0.9891, 0.9928, 0.9953]


def finite_diff(bias, n):
    """
    Рекурсивная функция для вычисления разделенных разностей.

    Args:
        bias (int): Смещение для работы с отдельными значениями из глобального списка y.
        n (int): Размер порядка разделенной разности.

    Returns:
        float: Результат вычисления разделенных разностей.
    """

    global y

    # Базовый случай: если n равно 1, вычисляем разность между двумя соседними значениями
    if n == 1:
        return y[bias + 1] - y[bias]

    # Рекурсивно вычисляем разделенную разность n-го порядка через n-1 порядок разностей
    return finite_diff(bias + 1, n - 1) - finite_diff(bias, n - 1)


def coef_q(q, num):

    def fact(n):
        factorial_result = 1
        while n > 1:
            factorial_result *= n
            n -= 1
        return factorial_result

    prod = q
    for i in range(1, num):
        prod *= q - i

    return prod/fact(num)


x_value = 1.43
h = 0.1
q = (x_value - x[4]) / h

print('Решение для условия x = 1.43')
print('За x0 берем x5 = 1.4')
result = y[4] + coef_q(q, 1)*finite_diff(4, 1) + coef_q(q, 2)*finite_diff(4, 2) + \
         coef_q(q, 3)*finite_diff(4, 3)
print('f(1.43) ≈ ', round(result, 5))

