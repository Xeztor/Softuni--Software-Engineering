nums = input()

data = nums.split()

for i in range(len(data)):
    if int(data[i]) > 0:
        data[i] = -int(data[i])
    else:
        data[i] = abs(int(data[i]))

print(data)
