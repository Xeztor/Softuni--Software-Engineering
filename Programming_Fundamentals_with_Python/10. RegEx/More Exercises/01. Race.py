from collections import Counter
import re

competitors = {name: 0 for name in input().split(', ')}

racer_data = input()
while not racer_data == 'end of race':
    name = ''.join([letter for letter in re.findall(r'[a-zA-Z]', racer_data)])
    distance = sum([int(km) for km in re.findall(r'\d', racer_data)])
    if name in competitors:
        competitors[name] += distance

    racer_data = input()

competitors = Counter(competitors)
top_3 = dict(competitors.most_common(3))

i = 1
for name in top_3:
    place = ''
    if i == 1:
        place = '1st'
    elif i == 2:
        place = '2nd'
    else:
        place = '3rd'

    print(f'{place} place: {name}')
    i += 1
