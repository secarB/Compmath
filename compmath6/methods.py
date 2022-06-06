from numpy import true_divide


def improved_euler_method(eq, h):
    n = int((eq.b - eq.a) / h)
    x, y = [eq.a], [eq.y0]
    for i in range(n):
        y.append(y[i] + h * eq.dif(x[i], y[i]))
        x.append(x[i] + h)

    return x, y


def milne_method(eq, h):
    n = int((eq.b - eq.a) / h)
    x, y = improved_euler_method(eq, h)
    f = eq.dif
    acc = 0.8
    for i in range(4, len(x)):
        k = [f(x[i - q], y[i - q]) for q in range(4)]
        while True:
            y1 = y[i-4] + 4*h/3*(2*k[2]-k[1]+2*k[0])
            y2 = y[i-2] + h/3 * (k[1]+4*k[0] + f(x[i], y1))
            if abs(y1-y2) < acc:
                y[i] = y[i-2] + h/3 * (k[1]+4*k[0] + f(x[i], y2))
                break
    return x, y


def runge_rule(yh, y2h, p):
    return abs((yh - y2h) / (2 ** p - 1))
