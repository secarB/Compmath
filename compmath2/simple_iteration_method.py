import numpy as np
from scipy.misc import derivative


def find_root_simple_iteration(f, start, stop, epsilon):
    print("__________________simple iteration__________________")
    l = find_lambda(f, start, stop)
    q = find_q(f, start, stop)
    print(f"lambda={round(l, 5)}, q=={round(q, 5)}")
    def phi(x): return x + f(x)*l
    print(f"phi(x) = x + f(x)*{round(l, 3)}")

    x0 = start
    x1 = phi(x0)
    xi = x1
    xi_prev = x0
    count = 0
    while float(abs(xi-xi_prev)) > epsilon:
        count = count + 1
        tmp = xi
        xi = phi(xi)
        xi_prev = tmp
    print("__________________simple iteration end__________________")
    print(f"n = {count}")
    print(f(xi))
    return xi


def find_lambda(f, start, stop):
    max_derivative = max(abs(derivative(f, start, dx=1e-8)),
                         abs(derivative(f, stop, dx=1e-8)))
    for i in np.arange(start, stop, 0.01):
        if max_derivative < abs(derivative(f, i, dx=1e-8)):
            max_derivative = abs(derivative(f, i, dx=1e-8))
    return -1/max_derivative


def find_q(f, start, stop):
    max_derivative = derivative(f, start, n=1, dx=1e-8)
    for i in np.arange(start, stop, 0.01):
        if max_derivative < abs(derivative(f, i, n=1, dx=1e-8)):
            max_derivative = abs(derivative(f, i, n=1, dx=1e-8))
    return max_derivative
