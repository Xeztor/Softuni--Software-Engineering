import re

text = []

while True:
    line = input()
    if line:
        text.append(line)
    else:
        break

text = '\n'.join(text)

pattern = r'\d+'
nums = re.findall(pattern, text)

print(*nums)
