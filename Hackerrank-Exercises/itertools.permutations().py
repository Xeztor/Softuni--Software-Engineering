# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, k = input().split()

perm = permutations(f"{''.join(sorted(s))}", int(k))

[print(''.join(row)) for row in perm]