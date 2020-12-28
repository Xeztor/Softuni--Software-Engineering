nums = input()
n = int(input())

data = list(map(int, nums.split()))
temp = data

for index, integer in enumerate(sorted(temp)):
    if index == n:
        break
    data.remove(integer)

print(data)
