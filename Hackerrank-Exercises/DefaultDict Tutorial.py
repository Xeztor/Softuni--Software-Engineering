from collections import defaultdict

n, m = list(map(int, input().split()))

words_indecies = defaultdict(list)
for i in range(1, n + 1):
    words_indecies[input()].append(i)

group_b = [input() for _ in range(m)]

for word in group_b:
    if word in words_indecies:
        print(*words_indecies[word])
    else:
        print('-1')
