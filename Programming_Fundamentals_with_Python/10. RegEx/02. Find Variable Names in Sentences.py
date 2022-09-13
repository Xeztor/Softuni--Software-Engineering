import re

data = input()

pattern = r'(^|(?<=\s))_(?P<varname>[A-Za-z0-9]+)\b'

print(','.join([i.group(2) for i in re.finditer(pattern, data)]))
