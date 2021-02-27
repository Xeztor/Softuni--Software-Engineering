def read_input_and_list_it(lines):
    elements = []
    for line in range(lines):
        elements.append(set(input().split()))

    return elements


lines_input = int(input())
elements = read_input_and_list_it(lines_input)
unique = set()
unique = unique.union(*elements)

[print(el) for el in unique]


