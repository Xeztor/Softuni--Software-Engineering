def recursive_power(n, power):
    if not power == 1:
        return recursive_power(n, power-1) * n
    else:
        return n


print(recursive_power(10, 100))
