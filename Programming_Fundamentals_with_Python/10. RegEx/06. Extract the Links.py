import re

pattern = r'www\.[a-zA-Z0-9-]+\.[a-z]+[a-z\.]+'

text = []
while True:
    data = input()
    if data:
        text.append(data)
    else:
        break

text = '\n'.join(text)
matches = re.finditer(pattern, text)
print(f'\n'.join([match.group() for match in matches]))
