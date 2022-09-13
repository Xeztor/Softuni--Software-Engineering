import re

current_block = ""

for i in range(int(input())):
    code_line = input()
    if '}' not in code_line:
        current_block += code_line
    else:
        [print(color) for color in re.findall(r'[\[;{(,]*(#(?:\b[0-9a-f]{3}\b|\b[0-9a-f]{6}\b))[;,})\]]', current_block, re.IGNORECASE)]
        current_block = ""
