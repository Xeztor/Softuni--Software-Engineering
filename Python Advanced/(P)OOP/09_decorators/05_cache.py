import functools


def cache(func):

    @functools.wraps(func)
    def wrapper(*args):
        log_key = int(args[0])
        if log_key not in wrapper.log:
            wrapper.log[log_key] = func(*args)
        return wrapper.log[log_key]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci.log)