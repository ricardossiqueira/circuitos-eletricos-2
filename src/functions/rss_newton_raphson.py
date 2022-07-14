def newton_raphson(f, df, x0, lim):
    '''
    f = function
    df = differential function
    x0 = initial guess
    lim = iteration limit
    '''

    i = 0

    while i <= lim:
        x1 = x0 - f(x0) / df(x0)
        x0 = x1
        i += 1

    return x1
