def factorial_num(num):
    factorial_sum = 1
    while num > 0:
        factorial_sum *= num
        num -= 1
    return factorial_sum


num1 = int(input())
num2 = int(input())
print(f"{factorial_num(num1) / factorial_num(num2):.2f}")
