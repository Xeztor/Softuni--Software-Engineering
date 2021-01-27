import re

string = input()

objects = re.finditer(r'(?=[^aeiou+\s-](?P<vowels>[aeiou]{2,})[^aeiou+\s-])', string, re.IGNORECASE)

result = []

for obj in objects:
    result.append(obj.group('vowels'))

if result:
    [print(el) for el in result]
else:
    print('-1')
