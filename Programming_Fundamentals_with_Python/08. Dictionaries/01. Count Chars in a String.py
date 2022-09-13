s = input()

occur = {}

for i in s:
    if not i == ' ':
        if i not in occur:
            occur[i] = 1
        else:
            occur[i] += 1

for key, value in occur.items():
    print(f'{key} -> {value}')
