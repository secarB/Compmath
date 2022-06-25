from linear import linear
from tools import minimized_deviation
from math import log


def logarimth(dots):
    data = {}

    n = len(dots)
    x = []
    for dot in dots:
        if dot[0] <= 0:
            return None
        x.append(dot[0])
    y = [dot[1] for dot in dots]

    linear_x = [log(x[i]) for i in range(n)]
    linear_result = linear([(linear_x[i], y[i]) for i in range(n)])

    a = linear_result['a']
    b = linear_result['b']
    data['a'] = a
    data['b'] = b

    def f(z): return a * log(z) + b
    data['f'] = f
    data['string'] = f"f = {round(a,3)}*ln(x) + {round(b,3)}"
    data['min_s'] = minimized_deviation(dots, f)
    return data
