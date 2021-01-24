import itertools

a_list = input()

an_iterator = itertools.groupby(a_list, lambda x: x[0])

l = []

for key, val in an_iterator:
    l.append(f'{(len(list(val)), int(key))}')

print(' '.join(l))
