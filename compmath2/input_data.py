

import numpy as np
from math import sin, exp
from system_solver import system_simple_iteration_method

from plt_helper import show_graph


def read_equation_console():
    print("Choose one of five equations:")
    print("1 -------- x^3 + 2*x^2 + 3*x (defalut)")
    print("2 -------- -x^3 +  7*x^2 - 3*x - 2")
    print("3 -------- x^3 - x + 4")
    print("4 -------- x^2 - 1")
    print("5 -------- -x^2 - 3*x + 3")

    match int(input()):
        case 1: equation = lambda x: x**3 + 2*x**2 + 3*x
        case 2: equation = lambda x: -x**3 + 7*x**2 - 3*x - 2
        case 3: equation = lambda x: x**3 - x + 4
        case 4: equation = lambda x: x**2 - 1
        case 5: equation = lambda x: -x**2 - 3*x + 3
        case _: equation = lambda x: x**3 + 2*x**2 + 3*x
    return equation


FUNCTIONS = [
    (
        (
            'f1(x1, x2) = 0.1 * x1^2 + x1 + 0.2 * x2^2 - 0.3',
            lambda x1, x2: 0.3 - 0.1 * x1 ** 2 - 0.2 * x2**2,
            lambda x1, x2: 0.1 * x1 ** 2 + x1 + 0.2 * x2 ** 2 - 0.3
        ),
        (
            'f1(x1, x2) = x1 - sin(2 * x2^2 + 3)',
            lambda x1, x2: sin(2 * x2 ** 2 + 3),
            lambda x1, x2: x1 - sin(2 * x2 ** 2 + 3)
        )
    ),
    (
        (
            'f2(x1, x2) = 0.2 * x1^2 + x2 + 0.1 * x1 * x2 - 0.7',
            lambda x1, x2: 0.7 - 0.2 * x1 ** 2 - 0.1 * x1 * x2,
            lambda x1, x2: 0.2 * x1 ** 2 + x2 + 0.1 * x1 * x2 - 0.7
        ),
        (
            'f2(x1, x2) = exp(x1^3 - 8 * x1^2) + 4 * x2',
            lambda x1, x2: -exp(x1 ** 3 - 8 * x1 ** 2) / 4,
            lambda x1, x2: exp(x1 ** 3 - 8 * x1 ** 2) + 4 * x2
        )
    )
]


def read_system():
    x = []
    y = []
    for i, group in enumerate(FUNCTIONS, 1):
        print(f'choose function')
        print(*(f'{j}. {fun[0]}' for j, fun in enumerate(group, 1)), sep='\n')
        n = int(input())
        x.append(group[n - 1][1])
        y.append(group[n - 1][2])
    x0 = list(map(float, def_input('Initial guesses',
              ' '.join(['1' for _ in x])).split()))
    eps = float(def_input('esp', 1e-3))

    return(x, x0, eps, y)


def def_input(prompt, def_value=None):
    v = input(f'{prompt} ({def_value}): ') if def_value is not None else input(
        f'{prompt}: ')
    return v if v.strip() else def_value


def read_interval_console():
    print("Enter the interval start float value")
    start = float(input())
    print("Enter the interval stop float value (notice, it has to be greater then start)")
    stop = float(input())

    if(stop <= start):
        print("Error! Stop has to be greater than start!")
        return read_interval_console()
    else:
        return start, stop


def read_epsilon_console():
    print("Enter accuracy:")
    return float(input())


def format_float(x):
    if isinstance(x, np.bool_):
        return x
    return f'{x:.3f}'


def read_method():
    print("Choose method to calculate root:")
    print("1 -------- Horse method")
    print("2 -------- Fixed point method")
    return int(input())
