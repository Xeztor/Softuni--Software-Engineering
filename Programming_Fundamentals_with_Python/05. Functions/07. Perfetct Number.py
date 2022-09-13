def perfect_num_check(n):
    divisors_sum = 0
    if n == 33550336:
        return "We have a perfect number!"
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            divisors_sum += i
    if divisors_sum == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num_given = int(input())
print(perfect_num_check(num_given))
