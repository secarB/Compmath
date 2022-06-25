from linear import linear
from tools import minimized_deviation
from math import log, exp


def power(dots):
    data = {}

    n = len(dots)
    x = []
    for dot in dots:
        if dot[0] <= 0:
            return None
        x.append(dot[0])
    y = []
    for dot in dots:
        if dot[1] <= 0:
            return None
        y.append(dot[1])

    linear_x = [log(x[i]) for i in range(n)]
    linear_y = [log(y[i]) for i in range(n)]
    linear_result = linear([(linear_x[i], linear_y[i]) for i in range(n)])

    a = exp(linear_result['b'])
    b = linear_result['a']
    data['a'] = a
    data['b'] = b

    def f(z): return a * (z ** b)
    data['f'] = f
    data['string'] = f"f = {round(a,3)}*x^{round(b,3)}"
    data['min_s'] = minimized_deviation(dots, f)
    return data
