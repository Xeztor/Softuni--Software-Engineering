from itertools import combinations

s, k = input().split()

s = sorted(s)

for i in range(1, int(k) + 1):
    [print(''.join(comb)) for comb in combinations(s, i)]