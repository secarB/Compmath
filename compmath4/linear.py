from tools import determinant
from tools import minimized_deviation
from math import sqrt


def linear(dots):
    data = {}

    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    x_avg = sum(x)/n
    y_avg = sum(y)/n
    r = sum([(x[i]-x_avg)*(y[i]-y_avg) for i in range(n)]) / \
        sqrt(sum([(x_i-x_avg)**2 for x_i in x])
             * sum([(y_i-y_avg)**2 for y_i in y]))

    sx = sum(x)
    sx2 = sum([xi ** 2 for xi in x])
    sy = sum(y)
    sxy = sum([x[i] * y[i] for i in range(n)])

    d = determinant([[sx2, sx],
                     [sx, n]])
    d1 = determinant([[sxy, sx],
                      [sy, n]])
    d2 = determinant([[sx2, sxy],
                      [sx, sy]])

    try:
        a = d1 / d
        b = d2 / d
    except ZeroDivisionError:
        return None
    data['a'] = a
    data['b'] = b

    def f(z): return a * z + b
    data['f'] = f
    data['string'] = f"f = {round(a,3)}*x + {round(b,3)}, r = {round(r,3)}"
    data['min_s'] = minimized_deviation(dots, f)
    return data
