import re

data = input()
data = re.split(r'[\s,]+', data)

demons = {}

for demon in data:
    name = demon
    health = sum([ord(letter) for letter in re.findall(r'[^0-9.+*/-]', demon)])
    nums = re.finditer(r'(?P<num>-?[\d]+(\.\d+)?)', demon)
    nums = [float(obj.group('num')) for obj in nums]
    attack = sum(map(float, nums))

    for delim in re.findall(r'[/*]', demon):
        if delim == '/':
            attack /= 2
        else:
            attack *= 2

    demons[name] = {'health': health, 'damage': attack}

for name, prop in sorted(demons.items(), key=lambda x: x[0]):
    print(f"{name} - {prop['health']} health, {prop['damage']:.2f} damage")
