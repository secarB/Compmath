from linear import linear
from tools import minimized_deviation
from math import log, exp


def exponent(dots):
    data = {}
    n = len(dots)
    x = [dot[0] for dot in dots]
    y = []
    for dot in dots:
        if dot[1] <= 0:
            return None
        y.append(dot[1])

    linear_y = [log(y[i]) for i in range(n)]
    linear_result = linear([(x[i], linear_y[i]) for i in range(n)])

    a = exp(linear_result['b'])
    b = linear_result['a']
    data['a'] = a
    data['b'] = b

    def f(z): return a * exp(b * z)
    data['f'] = f
    data['string'] = f"f = {round(a,3)}*e^({round(b,3)}*x)"
    data['min_s'] = minimized_deviation(dots, f)
    return data
