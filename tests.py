a = '6,15-6,8'.split('-')


first = a[0]
second = a[1]

for pair in a:
    pair = list(map(int, pair.split(',')))
    print(set(range(min(pair), max(pair))))