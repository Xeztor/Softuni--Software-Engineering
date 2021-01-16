n = int(input())
nums = input().split()
print(any(num for num in nums if num == num[-1::-1]) and all([int(num) > 0 for num in nums]))
