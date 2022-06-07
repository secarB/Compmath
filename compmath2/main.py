
import numpy as np
import matplotlib.pyplot as plt

from input_data import *
from simple_iteration_method import find_root_simple_iteration
from secant_method import find_root_secant

equation = read_equation_console()
start, stop = read_interval_console()
epsilon = read_epsilon_console()
match read_method():
    case 1:
        root = find_root_secant(equation, start, stop, epsilon)
        if root == None:
            print("Invalide interval and equation for scant calculation method")
    case 2:
        root = find_root_simple_iteration(equation, start, stop, epsilon)
        if root == None:
            print(
                "Invalide interval and equation for simple iteration calculation method")
    case _:
        print("Error with choosing method!")
if root != None:
    print(f"root={root} in [{start}, {stop}]")
    plt.plot([i for i in np.arange(start, stop, 0.01)], [equation(i)
             for i in np.arange(start, stop, 0.01)])
    plt.plot(root, equation(root), 'o')
    plt.title(f"Root in [{start},{stop}]")
    plt.show()
x, x0, eps, y = read_system()
res = system_simple_iteration_method(x, x0, eps)

if res.solved:
    print('result: ' + ' '.join(format_float(x) for x in res.roots))
    print('error: ' + ' '.join(str(x) for x in res.errors))
    print(f'Number of iterations {res.iteration}')
else:
    print('No solutions found')
bx = abs(min(res.roots)) + 1
show_graph(bx, 0, y, [])
exit(0)
