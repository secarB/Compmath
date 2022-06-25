def lagrange_interpolation(x, y, point):
    result = {
        "name": "lagrange interpolation",
        "x": point,
        "y": 0
    }
    n = len(x)
    for i in range(n):
        numerator = denominator = 1
        for j in range(n):
            if i != j:
                numerator *= point-x[j]
                denominator *= x[i]-x[j]
        result["y"] += y[i] * numerator/denominator
    return result
