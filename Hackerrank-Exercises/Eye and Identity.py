def sum_p(coefficients, x):
    result = 0
    for i in range(len(coeffs)):
        result += coeffs[i] * x ** (len(coeffs) - 1 - i)
    return result


coeffs = list(map(float, input().split()))
x = int(input())
print(sum_p(coeffs, x))


