from collections import Counter
import re

s = input()

letters = re.findall(r'.', s)
occur = Counter(sorted(letters))

for letter, occurrences in sorted(occur.most_common(3), key=lambda x: (-x[1], x[0])):
    print(letter, occurrences)
