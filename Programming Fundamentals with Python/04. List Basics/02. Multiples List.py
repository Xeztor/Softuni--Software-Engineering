factor = int(input())
count = int(input())

data = []

for i in range(factor, factor * count + 1, factor):
    data.append(i)

print(data)
