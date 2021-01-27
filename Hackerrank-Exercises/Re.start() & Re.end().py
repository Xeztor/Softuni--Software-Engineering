import re


string = input()

word_searching = input()


match_objects = re.finditer(rf'(?=({word_searching}))', string)

result_l = []
for obj in match_objects:
    result_l.append((obj.start(), obj.start() + len(word_searching) - 1))

if result_l:
    [print(el) for el in result_l]
else:
    print((-1, -1))
