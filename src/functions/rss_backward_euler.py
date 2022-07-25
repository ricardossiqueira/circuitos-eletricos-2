def backward_euler(f, x, y, h):
    """
    Solves the differential equation y' = f(x, y) using the backward
    Euler method.
    """
    y_new = y + h * f(x, y)
    return y_new
