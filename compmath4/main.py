from tools import plot
from linear import linear
from quadratic import quadratic
from power import power
from exponent import exponent
from logarimth import logarimth
from cube import cube
import numpy as np

FILE_IN = "../input"
FILE_OUT = "output"


def get_input():
    print("Enter \"x y\".")
    data = []
    while True:
        try:
            ip = input().strip()
            if ip == '.':
                if len(data) < 2:
                    raise ValueError
                break
            dot = tuple(map(float, ip.split()))
            if len(dot) != 2:
                raise TypeError
            data.append(dot)
        except TypeError:
            print("Please type by \"x y\"")
        except ValueError:
            print("Please add at least 2 points")
    return data


def main():
    data = get_input()
    tmp = [linear(data), quadratic(data),  cube(data),
           exponent(data), logarimth(data), power(data)]
    results = [result for result in tmp if result is not None]

    print("\n{:<50}{:<15}".format('Function', 'Deviation'))
    for result in results:
        print("{:<50}{:<15}".format(result['string'], result['min_s']))

    x = np.array([dot[0] for dot in data])
    y = np.array([dot[1] for dot in data])
    plot_x = np.linspace(np.min(x), np.max(x), 100)
    plot_y = []
    labels = []
    for result in results:
        plot_y.append([result['f'](x) for x in plot_x])
        labels.append(result['string'])
    plot(x, y, plot_x, plot_y, labels)

    final_result = min(results, key=lambda a: a['min_s'])
    print("\nthe best result: ", final_result['string'])

    return 0


main()
