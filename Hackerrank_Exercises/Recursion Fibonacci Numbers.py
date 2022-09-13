def fibonacci(n):
    if not n < 3:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return 1


# n = int(input())
print(fibonacci(2))