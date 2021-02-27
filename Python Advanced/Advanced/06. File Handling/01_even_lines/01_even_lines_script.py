import re


data = []

with open('text.txt', 'r') as file:
    data = file.readlines()

for i in range(len(data)):
    if i % 2 == 0:
        changed = re.sub(r'[,.!?-]', '@', data[i])
        reversed_line = changed[:-1].split()[::-1]
        print(' '.join(reversed_line))
