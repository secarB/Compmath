from newton import newton_interpolation
from lagrange import lagrange_interpolation
import matplotlib.pyplot as plt
from math import sin, log


def get_data():
    print("Method enter nodes: \n1 - manually (by default) \n2 - from available functions")
    match (int(input())):
        case 1: data = manually()
        case 2: data = from_functions()
        case _: data = manually()

    data.sort()
    print(f"Nodes:", data)
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    nodes = {"x": x, "y": y}

    print("Method interpolation (both by default):")
    print("1 - Newton")
    print("2 - Lagrange")
    method = int(input())

    print("Interpolated point:")
    while True:
        point = float(input())
        if point < x[0] or point > x[len(x)-1]:
            print("Point has to be in range of x_min to x_max")
        else:
            break

    return nodes, method, point


def manually():
    print("Enter nodes seperated by lines (x y), \'.\' to finish:")
    data = []
    while True:
        line = input()
        if (line == "."):
            break
        values = line.strip().split()
        if (len(values) == 2):
            data.append((float(values[0]), float(values[1])))
        else:
            print("Enter nodes seperated by lines (x y), \'.\' to finish:")
    return data


def from_functions():
    print("Choose function:")
    print("1 - sin(x) (by default)")
    print("2 - x^2-3x+5")
    print("3 - log(x) (x_min>0)")
    match (int(input())):
        case 1: f = lambda x: sin(x)
        case 2: f = lambda x: x**2-3*x+5
        case 3: f = lambda x: log(x)
        case _: f = lambda x: sin(x)

    print("Enter the range (x_min x_max):")
    while True:
        values = input().strip().split()
        if (len(values) == 2 and values[1] > values[0]):
            bounds = (float(values[0]), float(values[1]))
            break
        else:
            print("Enter the range (x_min x_max):")

    print("Number of nodes (n>=2):")
    while True:
        n = int(input())
        if n < 2:
            print("Number of nodes (n>=2):")
        else:
            break

    h = abs(bounds[1] - bounds[0]) / n
    data = []
    [data.append((bounds[0] + h * i, f(bounds[0] + h * i))) for i in range(n)]
    return data


def plotting(x, y, *results):
    for result in results:
        plt.plot([result["x"]], [result["y"]],
                 marker="o", label=result["name"])
    plt.plot(x, y, marker=".", label="input data")
    plt.legend()
    plt.show()


def main():
    nodes, method, point = get_data()
    x = nodes["x"]
    y = nodes["y"]
    match (method):
        case 1:
            result = newton_interpolation(x, y, point)
            print(result)
            plotting(x, y, result)
        case 2:
            result = lagrange_interpolation(x, y, point)
            print(result)
            plotting(x, y, result)
        case _:
            newton = newton_interpolation(x, y, point)
            lagrange = lagrange_interpolation(x, y, point)
            print(newton)
            print(lagrange)
            plotting(x, y, newton, lagrange)


main()
