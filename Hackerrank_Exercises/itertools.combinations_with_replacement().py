from itertools import combinations_with_replacement

string, k = input().split()

sorted_comb = combinations_with_replacement(sorted(list(string)), int(k))
[print(''.join(comb)) for comb in sorted_comb]
