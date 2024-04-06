from sympy import symbols, simplify, expand

x = [0, 1, 2, 3, 4, 5]
y = [5.2, 8.0, 10.4, 12.4, 14.0, 15.2]


def simplify_expression(expression):
    x, y = symbols('x y')
    expr = eval(expression)
    expanded_expr = expand(expr, mul=True)
    simplified_expr = simplify(expanded_expr)
    return str(simplified_expr)


def finite_diff(bias, n):
    global y
    if n == 1:
        return y[bias + 1] - y[bias]
    return finite_diff(bias + 1, n - 1) - finite_diff(bias, n - 1)


def fact(n):
    factorial_result = 1
    while n > 1:
        factorial_result *= n
        n -= 1
    return factorial_result


h = 1
q = f'(x - {x[0]})/{h}'
expression = f"{y[0]} + {finite_diff(0, 1)}*{q} + {round(finite_diff(0, 2) / fact(2), 5)}*{q}*({q}-1)"
result = simplify_expression(expression)
print(result)
