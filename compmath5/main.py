import numpy as np
import matplotlib.pyplot as plt
from math import sin, sqrt

from interpolation import *


class Fun:
    def __init__(self, expr):
        self.__expr = expr

    def __call__(self, x):
        return eval(self.__expr)

    def __str__(self):
        return self.__expr


FUNCTIONS = [
    Fun('2 * x**2 - 8 * x + 1'),
    Fun('sqrt(x) / 2'),
    Fun('sin(x)')
]


def read_table():
    dots = []

    print('Enter the table.')
    print('Enter to end.')
    while (line := input()) != '':
        dots.append(tuple(map(float, line.split())))

    return dots


def read_func():
    print('Choose function.')
    for i, fun in enumerate(FUNCTIONS, 1):
        print(f'{i}. {fun!s}')
    func_id = int(input('Function number: '))
    func = FUNCTIONS[int(func_id) - 1]

    a, b = map(float, input('a-b: ').split())
    a, b = min(a, b), max(a, b)

    n = int(input('Number of interpolation: '))

    return space(func, a, b, n)


def plot(x, y, plot_x, plot_y, x0, answer):
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.plot(1, 0, marker='>', ms=5, color='k',
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, marker='^', ms=5, color='k',
            transform=ax.get_xaxis_transform(), clip_on=False)

    plt.plot(x, y, 'o', plot_x, plot_y)
    plt.plot([x0], [answer], 'o', markeredgecolor='red',
             markerfacecolor='green')
    plt.show()


def space(f, a, b, n):
    dots = []
    h = (b - a) / (n - 1)
    for i in range(n):
        dots.append((a, f(a)))
        a += h
    return dots


def get_input():
    print('Choose mehod.')
    print('1. Lagrange polynomial')
    print('2. Gaussian polynomial')
    method = int(input('Solution method: ').strip())

    print('Choose input type.')
    print('1. Point set')
    print('2. Function')
    input_method = int(input('Type: '))

    dots = (read_table, read_func)[input_method - 1]()
    x = float(input('Argument value to interpolate:: '))

    return method, dots, x


def main():
    method, dots, x0 = get_input()
    x = np.array([dot[0] for dot in dots])
    y = np.array([dot[1] for dot in dots])
    plot_x = np.linspace(np.min(x), np.max(x), 100)

    res = (
        (lambda: lagrange_polynomial(dots, x0),
         lambda: [lagrange_polynomial(dots, x_) for x_ in plot_x]),
        (lambda: gauss_polynomial(dots, x0),
         lambda: [lagrange_polynomial(dots, x_) for x_ in plot_x]),
    )[method - 1]
    answer, plot_y = map(lambda f: f(), res)

    plot(x, y, plot_x, plot_y, x0, answer)

    print(f'Approximate function value: {answer}')


main()
