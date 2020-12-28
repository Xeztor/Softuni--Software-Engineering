import re

sentence = input()
word = input().lower()

pattern = rf'\b{word}\b'

print(len(list(re.finditer(pattern, sentence, re.IGNORECASE))))
