def newton_raphson(f, df, x, epsilon, lim):
    '''
    f = function
    df = differential function
    x = initial guess
    epsilon = error tolerance
    lim = iteration limit
    '''

    for _ in range(lim):
        x = x - f(x) / df(x)
        if abs(f(x)) < epsilon:
            return x

    return x
