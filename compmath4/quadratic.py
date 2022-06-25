from tools import determinant
from tools import minimized_deviation


def quadratic(dots):
    data = {}

    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]

    sx = sum(x)
    sx2 = sum([xi ** 2 for xi in x])
    sx3 = sum([xi ** 3 for xi in x])
    sx4 = sum([xi ** 4 for xi in x])
    sy = sum(y)
    sxy = sum([x[i] * y[i] for i in range(n)])
    sx2y = sum([(x[i] ** 2) * y[i] for i in range(n)])

    d = determinant([[n, sx, sx2],
                     [sx, sx2, sx3],
                     [sx2, sx3, sx4]])
    d1 = determinant([[sy, sx, sx2],
                      [sxy, sx2, sx3],
                      [sx2y, sx3, sx4]])
    d2 = determinant([[n, sy, sx2],
                      [sx, sxy, sx3],
                      [sx2, sx2y, sx4]])
    d3 = determinant([[n, sx, sy],
                      [sx, sx2, sxy],
                      [sx2, sx3, sx2y]])
    try:
        c = d1/d
        b = d2/d
        a = d3/d
    except ZeroDivisionError:
        return None
    data['c'] = c
    data['b'] = b
    data['a'] = a
    def f(z): return a*(z**2) + b*z + c
    data['f'] = f
    data['string'] = f"f = {round(a,3)}*x^2 + {round(b,3)}*x + {round(c,3)}"
    data['min_s'] = minimized_deviation(dots, f)
    return data
