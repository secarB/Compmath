import numpy as np
from scipy.misc import derivative


def find_root_secant(f, start, stop, epsilon):
    if not check_interval(f, start, stop):
        return None
    x0 = choose_x0(f, start)
    x1 = x0 - f(x0) / derivative(f, x0, n=1)
    xi = x1
    xi_prev = x0
    count = 0
    while(abs(xi - xi_prev) > epsilon):
        count = count + 1
        tmp = xi
        xi = xi - f(xi) * (xi - xi_prev) / (f(xi) - f(xi_prev))
        xi_prev = tmp
    print(f"n = {count}")
    print(f(xi))
    return xi


def check_interval(equation, start, stop):
    if not equation(start)*equation(stop) < 0:
        return False
    start_derivative_fst = derivative(equation, start, n=1, dx=1e-8)
    start_derivative_snd = derivative(equation, start, n=2, dx=1e-8)
    for i in np.arange(start, stop, 0.01):
        if not ((start_derivative_fst*derivative(equation, i, n=1, dx=1e-8) > 0)
                and (start_derivative_snd*derivative(equation, i, n=2) >= 0)):
            print(f"start_fst={start_derivative_fst}, start_snd={start_derivative_snd}, derivative(n=1)={derivative(equation, i, n=1)} derivative(n=2)={derivative(equation, i, n=2)}")
            return False
    return True


def choose_x0(equation, start):
    start_derivative_snd = derivative(equation, start, n=2, dx=1e-8)
    if(start_derivative_snd*start > 0):
        return start
    else:
        return True
