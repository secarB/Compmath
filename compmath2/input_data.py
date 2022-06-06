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


def read_method():
    print("Choose method to calculate root:")
    print("1 -------- Horse method")
    print("2 -------- Fixed point method")
    return int(input())
