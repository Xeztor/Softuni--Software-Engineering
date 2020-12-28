def sum_numbers(n1, n2):
    nums_list = [n1, n2]
    return sum(nums_list)


def subtract(n1, n2):
    return n1 - n2


def add_and_subtract():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    return subtract(sum_numbers(num1, num2), num3)


print(add_and_subtract())
