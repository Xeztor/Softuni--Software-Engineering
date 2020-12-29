import math
import os
import random
import sys



s = input()

from collections import Counter
import re

letters = re.findall(r'.', s)
occur = Counter(sorted(letters))

for letter, occurrences in sorted(occur.most_common(3), key=lambda x: (-x[1], x[0])):
    print(letter, occurrences)
