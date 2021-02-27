def read_input(queries):
    name_values = []
    for line in range(1, queries + 1):
        name = input()
        name_values.append(sum([ord(letter) for letter in name]) // line)

    return name_values


def odd_even_set(values):
    odd, even = set(), set()
    for val in values:
        if val % 2 == 0:
            even.add(val)
        else:
            odd.add(val)

    return odd, even


def print_resulting_set(resulting_set):
    print(', '.join(list(map(str, resulting_set))))


queries = int(input())
name_values = read_input(queries)
odd, even = odd_even_set(name_values)

if sum(even) == sum(odd):
    print_resulting_set(odd.union(even))
elif sum(odd) > sum(even):
    print_resulting_set(odd.difference(even))
elif sum(odd) < sum(even):
    print_resulting_set(odd.symmetric_difference(even))
