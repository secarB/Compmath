from math import factorial


def lagrange_polynomial(dots, x):
    result = 0
    n = len(dots)
    for i in range(n):
        nom, denom = 1, 1
        for j in range(n):
            if i == j:
                continue
            nom *= x - dots[j][0]
            denom *= dots[i][0] - dots[j][0]
        result += dots[i][1] * nom / denom

    return result


def gauss_t(t, n):
    tmp = t
    for i in range(1, n):
        tmp *= t + ((-1) ** i) * ((i + 1) // 2)
    return tmp


def gauss_polynomial(dots, x):
    n = len(dots)
    y = [[0 for _ in range(n)] for __ in range(n)]
    for k in range(n):
        y[k][0] = dots[k][1]

    for i in range(1, n):
        for j in range(n - 1):
            y[j][i] = y[j + 1][i - 1] - y[j][i - 1]

    result = y[n // 2][0]
    t = (x - dots[n // 2][0]) / (dots[1][0] - dots[0][0])
    for i in range(1, n):
        result += gauss_t(t, i) * y[(n - i) // 2][i] / factorial(i)

    return result
