def get_odd(numbers):
    return [num for num in numbers if not num % 2 == 0]


def get_even(numbers):
    return [num for num in numbers if num % 2 == 0]


cmd = input()
nums = list(map(int, input().split()))

if cmd == 'Odd':
    print(sum(get_odd(nums)) * len(nums))
elif cmd == 'Even':
    print(sum(get_even(nums)) * len(nums))
