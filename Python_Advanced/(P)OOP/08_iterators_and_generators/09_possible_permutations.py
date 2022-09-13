from itertools import permutations


def possible_permutations(seq):
    for p in permutations(seq):
        yield list(p)


a = 'abc'

for i in possible_permutations(a):
    print(i)