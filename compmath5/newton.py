from math import factorial


def newton_interpolation(x, y, point):
    result = {
        "name": "newton interpolation",
        "x": point
    }
    if const_h(x):
        result["y"] = newton_for_equidistant_nodes(x, y, point)
    else:
        result["y"] = newton_for_nonequidistant_nodes(x, y, point)
    return result


def newton_for_equidistant_nodes(x, y, point):
    n = len(x)
    h = abs(x[1] - x[0])

    difs = [[0] * n for _ in range(n)]
    for i in range(n):
        difs[i][0] = y[i]
    k = 1
    while k <= n:
        for i in range(n - k):
            difs[i][k] = round(difs[i + 1][k - 1] - difs[i][k - 1], 5)
        k += 1
    print(difs)

    if point <= x[n // 2]:
        i0 = 0
        for i in range(1, n):
            if point > x[i]:
                i0 += 1
            else:
                break
        t = (point - x[i0])/h
        result = difs[i0][0]
        for i in range(1, n):
            result += (product_t_backward(t, i)*difs[i0][i])/factorial(i)
    else:  # second formula (the last node as the anchor)
        t = (point - x[n-1])/h
        result = difs[n - 1][0]
        for i in range(1, n):
            result += (product_t_forward(t, i)*difs[n-i-1][i])/factorial(i)

    return result


def newton_for_nonequidistant_nodes(x, y, point):
    n = len(x)
    difs = [[0] * n for _ in range(n)]
    for i in range(n):
        difs[i][0] = y[i]
    k = 1
    while k <= n:
        for i in range(n - k):
            difs[i][k] = round(
                (difs[i+1][k-1] - difs[i][k-1])/(x[i+k] - x[i]), 5)
        k += 1
    return y[0] + sum([difs[0][k] * product([point - x[i] for i in range(k)]) for k in range(1, n)])


def product_t_backward(t_0, i):
    t = t_0
    for j in range(1, i):
        t *= t_0 - j
    return t


def product_t_forward(t_0, i):
    t = t_0
    for j in range(1, i):
        t *= t_0 + j
    return t


def product(list):
    result = 1
    for x in list:
        result = result * x
    return result


def const_h(x):
    h = abs(x[1] - x[0])
    e = 0.01
    for i in range(len(x) - 1):
        if abs(abs(x[i + 1] - x[i]) - h) > e:
            return False
    return True
