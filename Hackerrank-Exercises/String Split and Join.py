def split_and_join(string):
    string = string.split()
    return '-'.join(string)


line = input()
result = split_and_join(line)
print(result)
