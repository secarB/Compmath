from math import sqrt
import matplotlib.pyplot as plt


def get_cofactor(matrix, i, j):
    n = len(matrix)
    return [[matrix[row][col] for col in range(n) if col != j] for row in range(n) if row != i]


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    det = 0
    sgn = 1
    for j in range(n):
        det += sgn * matrix[0][j] * determinant(get_cofactor(matrix, 0, j))
        sgn *= -1
    return det


def deviation(dots, f):
    n = len(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    return sum([(f(x[i]) - y[i])**2 for i in range(n)])


def minimized_deviation(dots, f):
    n = len(dots)
    return sqrt(deviation(dots, f) / n)


def plot(x, y, plot_x, plot_y, labels):
    plt.plot(x, y, 'o')
    for i in range(len(plot_y)):
        plt.plot(plot_x, plot_y[i], label=labels[i])
    plt.legend()
    plt.show()
