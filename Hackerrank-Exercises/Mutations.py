def mutate_string(string, position, character):
    new_str = string[:position] + f"{character}" + string[position + 1:]
    return new_str


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)