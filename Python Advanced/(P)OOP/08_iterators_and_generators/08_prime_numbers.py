from math import sqrt


def get_primes(nums):
    for n in nums:
        is_prime = True
        for divisor in range(2, int(sqrt(n) + 1)):
            if n % divisor == 0:
                is_prime = False
        if is_prime:
            yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
