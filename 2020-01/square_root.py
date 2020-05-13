def square_root(x):
    if x == 0:
        return 0
    eps = 0.0001
    end = x
    start = 0
    candidate = end - (end - start) / 2
    sqr = candidate ** 2
    while abs(sqr - x) > eps:
        if sqr > x:
            end = candidate
        else:
            start = candidate
        candidate = end - (end - start) / 2
        sqr = candidate ** 2
    return candidate


for x in range(101):
    print(x, square_root(x))

