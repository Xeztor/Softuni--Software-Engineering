flag = False

requirements = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}

while not flag:
    data = input().split()
    for _ in range(len(data) // 2):
        val = int(data.pop(0))
        key = data.pop(0).lower()
        if key in requirements and requirements[key] + val < 250:
            requirements[key] += val
        elif key in requirements and requirements[key] + val >= 250:
            flag = True
            requirements[key] += val - 250
            if key == 'shards':
                legendery_item = 'Shadowmourne'
            elif key == 'fragments':
                legendery_item = 'Valanyr'
            else:
                legendery_item = 'Dragonwrath'
            print(f'{legendery_item} obtained!')
            break
        else:
            if key not in junk:
                junk[key] = val
            else:
                junk[key] += val


requirements = {k: v for k, v in sorted(requirements.items(), key=lambda x: (-x[1], x[0]))}
junk = {k: v for k, v in sorted(junk.items(), key=lambda x: x[0])}

for k, v in requirements.items():
    print(f'{k}: {v}')

for k, v in junk.items():
    print(f'{k}: {v}')
