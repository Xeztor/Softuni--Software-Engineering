data = input()

result = []

for i in data:
    if result:
        if not i == result[-1]:
            result.append(i)
    else:
        result.append(i)

print(''.join(result))
