def outer():
    def inner(x):
        return x + 3
    return inner
