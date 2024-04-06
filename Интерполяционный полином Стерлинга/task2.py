import matplotlib.pyplot as plt
import numpy as np

x = [4, 5, 6, 7, 1, 2, 3]
y = [15, 20, 22, 24, 2, 5, 10]


def fact(n):
    factorial_result = 1
    while n > 1:
        factorial_result *= n
        n -= 1
    return factorial_result


def finite_diff(bias, n):
    global y
    if n == 1:
        return y[bias + 1] - y[bias]
    elif n <= 0:
        return y[0]
    return finite_diff(bias + 1, n - 1) - finite_diff(bias, n - 1)


def product(i, u):
    # Если переданный параметр меньше 1, вернуть 1
    if i < 1:
        return 1

    # Иначе вычислить произведение от j=1 до n
    prod = 1
    for j in range(1, i + 1):
        prod *= u ** 2 - j ** 2

    return prod


def stirling_polynomial(x_value, h):
    result = y[0]
    u = round((x_value - x[0]) / h, 3)
    n = int((len(x) - 1) / 2)
    for i in range(1, n+1):
        result += (u / fact(2 * i - 1)) * \
                  (product(i - 1, u) * (finite_diff(-(i-1), 2*i-1) + finite_diff(-i, 2*i-1)) / 2) + \
                  ((u**2/fact(2*i))*product(i-1, u)*finite_diff(-i, 2*i))

    return result

h = 1
x_value = 4.3
result = stirling_polynomial(x_value, h)
print(round(result, 5))

# Подготовим данные для графика
x_points = np.linspace(min(x), max(x), 100)
y_points = [stirling_polynomial(point, h) for point in x_points]

plt.figure(figsize=(10, 6))
plt.plot(x_points, y_points, label="Stirling Polynomial Interpolation")
plt.scatter(x, y, color='red', label="Data Points")
plt.scatter(x_value, result, color='green', label="Interpolated Point (x=4.3)")

plt.xlabel('x')
plt.ylabel('Interpolated f(x)')
plt.title('Stirling Polynomial Interpolation')
plt.legend()
plt.grid(True)
plt.show()
