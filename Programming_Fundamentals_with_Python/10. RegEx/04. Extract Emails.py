import re

data = input()
pattern = r'(^|(?<=\s))(?P<user>\b[a-z]+[_.-]?[a-z]+)@(?P<domain>[a-z]+-?[a-z]+\.[a-z]+(\.[a-z]+)?)'
print('\n'.join([f'{i.group(2)}@{i.group(3)}' for i in re.finditer(pattern, data)]))
