import itertools
import re
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2


n = int(input())
letters = re.sub(r'\s', '', input())
k = int(input())
letters_to_match = letters[:k + 1]

data = itertools.combinations(letters, k)
matching = 0
for letter in letters_to_match:
    for el in data:
        if 'a' in el:
            matching += 1

print(f'{matching / ncr(n, k):.4f}')
