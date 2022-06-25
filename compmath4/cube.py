from tools import determinant
from tools import minimized_deviation


def cube(dots):
    data = {}

    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]

    sx = sum(x)
    sx2 = sum([xi ** 2 for xi in x])
    sx3 = sum([xi ** 3 for xi in x])
    sx4 = sum([xi ** 4 for xi in x])
    sx5 = sum([xi ** 5 for xi in x])
    sx6 = sum([xi ** 6 for xi in x])
    sy = sum(y)
    sxy = sum([x[i] * y[i] for i in range(n)])
    sx2y = sum([(x[i] ** 2) * y[i] for i in range(n)])
    sx3y = sum([(x[i] ** 3) * y[i] for i in range(n)])

    de = determinant([[n, sx, sx2, sx3],
                     [sx, sx2, sx3, sx4],
                     [sx2, sx3, sx4, sx5],
                     [sx3, sx4, sx5, sx6]])
    de1 = determinant([[sy, sx, sx2, sx3],
                       [sxy, sx2, sx3, sx4],
                       [sx2y, sx3, sx4, sx5],
                       [sx3y, sx4, sx5, sx6]])
    de2 = determinant([[n, sy, sx2, sx3],
                       [sx, sxy, sx3, sx4],
                       [sx2, sx2y, sx4, sx5],
                       [sx3, sx3y, sx5, sx6]])
    de3 = determinant([[n, sx, sy, sx3],
                       [sx, sx2, sxy, sx4],
                       [sx2, sx3, sx2y, sx5],
                       [sx3, sx4, sx3y, sx6]])
    de4 = determinant([[n, sx, sx2, sy],
                       [sx, sx2, sx3, sxy],
                       [sx2, sx3, sx4, sx2y],
                       [sx3, sx4, sx5, sx3y]])
    try:
        d = de1/de
        c = de2/de
        b = de3/de
        a = de4/de
    except ZeroDivisionError:
        return None
    data['d'] = d
    data['c'] = c
    data['b'] = b
    data['a'] = a
    def f(z): return a*(z**3) + b*(z**2) + c*z + d
    data['f'] = f
    data['string'] = f"f = {round(a, 3)}*x^3 + {round(b, 3)}*x^2 + {round(c, 3)}*x + {round(d, 3)}"
    data['min_s'] = minimized_deviation(dots, f)
    return data
