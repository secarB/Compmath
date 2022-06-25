import math

from integral_solver import (
    rect_method,
    trapezoidal_method,
    runge_err,
)

k = 2


def ask(functions):
    print('Enter the function:')
    for i, fun in enumerate(functions, 1):
        print(f"{i}. {fun['s']}")

    fun_i = int(input())
    if not 1 <= fun_i <= len(functions):
        print('Неверное значение')

    fun = functions[fun_i - 1]
    f, F, s = fun['f'], fun['F'], fun['s']

    print(f'''Choose the method: {fun["s"]}
            1. Left rectangle method
            2. Method of middle rectangles
            3. Right rectangle method
            4. Trapezoidal method'''
          )

    method = int(input())
    a, b = map(float, input(
        'Enter integration limits separated by a space: ').split())
    n = int(input('Enter number of splits: '))
    esp = float(input('Enter error: '))
    return f, F, s, method, a, b, n, esp


def main():
    functions = [
        {
            'f': lambda x: -x ** 3 - x ** 2 - 2 * x + 1,
            'F': lambda x: -x ** 4 / 4 - x ** 3 / 3 - x ** 2 + x,
            's': '-x^3 - x^2 - 2x + 1'
        },
        {
            'f': lambda x: -4 * x ** 3 - 3 * x ** 2 - 2 * x + 10,
            'F': lambda x: -x ** 4 - x ** 3 - x ** 2 + 10 * x,
            's': '-4x^3 - 3x^2 - 2x + 10'
        },
        {
            'f': lambda x: -8 * x ** 3 - 6 * x ** 2 - 4 * x - 8,
            'F': lambda x: -2 * x ** 4 - 2 * x ** 3 - 2 * x ** 2 - 8 * x,
            's': '-8x^3 - 6x^2 - 4x - 8'
        }
    ]

    f, F, s, method, a, b, n, esp = ask(functions)
    fun = None
    err_f = 0
    match method:
        case 1 | 2 | 3:
            def fun(): return rect_method(f, a, b, method - 2, n)
            def err_f(): return rect_method(f, a, b, method - 2, n // 2)
        case 4:
            def fun(): return trapezoidal_method(f, a, b, n)
            def err_f(): return trapezoidal_method(f, a, b, n // 2)
    res = fun()
    if method == 4:
        s = trapezoidal_method(f, a, b, n*2)
        while (abs(res - s) > esp):
            res = s
            n = n * 2
            s = trapezoidal_method(f, a, b, n*2)
        res2 = trapezoidal_method(f, a, b, n//2)
    else:
        s = rect_method(f, a, b, method-2, n*2)
        while (abs(res - s) > esp):
            res = s
            n = n * 2
            s = rect_method(f, a, b, method-2, n*2)
        res2 = rect_method(f, a, b, method-2, n // 2)
    print('Calculation result:', res)
    print('Number of splits:', n)

    err_abs = abs(F(b) - F(a) - res)
    print(f'error: {err_abs:.4f} ({abs(err_abs / (F(b) - F(a))):.2f}%)')

    res2 = err_f()
    err = runge_err(res, res2, k)
    print(f'Runge error: {err:.4f}')
    print('According to the Newton-Leibniz method:', F(b) - F(a))


def get_end_result(result):
    if not isinstance(result, tuple):
        return result

    status, res = result
    if status:
        return res

    return get_end_result(res)


if __name__ == '__main__':
    main()
