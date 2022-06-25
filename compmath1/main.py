def solve_task1():
    def Y(x): return 3 * x / (x ** 4 + 6)
    X_FROM, X_TO = 0, 2
    H = 0.2

    import task1
    task1.solve(Y, X_FROM, X_TO, H)


if __name__ == '__main__':
    import approx
    from io_helper import (
        read_data_from_console,
        read_data_from_file,
        output,
        show_graph
    )

    approxes = [
        ('Linear function', approx.approx_lin),
        ('Quadratic function', approx.approx_quad),
        ('Cubic function', approx.approx_cube),
        ('Exponential Function', approx.approx_exp),
        ('Logarithmic function', approx.approx_log),
        ('Power function', approx.approx_pow),
    ]

    read_mode = input('File input (_): ').strip()
    read = ((lambda: read_data_from_file(read_mode))
            if read_mode
            else read_data_from_console)
    xs, ys = read()

    results = [a[1](xs, ys) for a in approxes]
    index_min = min(range(len(results)), key=results.__getitem__)

    write_mode = input('File output: ').strip()
    file = open(write_mode, 'w') if write_mode else None

    def out(x): return output(x, file)

    for i, result in enumerate(results):
        name = approxes[i][0]
        out(f'--- {name}')
        out(f'φ(x) = {result.function_str}')
        out(f'S = {result.dispersion:.3f}')
        out(f'δ = {result.deviation:.3f}')
        out(f'R^2 = {result.confidence:.3f}')
        if result.pearson:
            out(f'r = {result.pearson:.3f}')

    out(f'Best approximates {approxes[index_min][0]}: '
        f'δ = {results[index_min].deviation:.3f}')

    show_graph(xs, ys, results)
