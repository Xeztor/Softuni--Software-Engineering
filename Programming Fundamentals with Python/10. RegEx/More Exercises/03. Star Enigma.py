import re

pattern = r'@(?P<name>[a-zA-Z]+)([^@!:>-]+)?:\d+([^@!:>-]+)?!(?P<action>[AD])!([^@!:>-]+)?->\d+'
n = int(input())

all_planets_data = {'attacked': [], 'destroyed': []}

for _ in range(n):
    encrypted = input()
    decrypt_coeff = len(re.findall(r'[star]', encrypted, re.IGNORECASE))
    decrypted = []

    for letter in encrypted:
        decrypted.append(chr(ord(letter) - decrypt_coeff))

    decrypted = ''.join(decrypted)
    planet_data = re.search(pattern, decrypted)
    if planet_data:
        planet_name, action = planet_data.group('name', 'action')
        if action == 'A':
            all_planets_data['attacked'].append(planet_name)
        else:
            all_planets_data['destroyed'].append(planet_name)

for action, planets in all_planets_data.items():
    if action == 'attacked':
        print(f'Attacked planets: {len(planets)}')
    else:
        print(f'Destroyed planets: {len(planets)}')

    for planet in sorted(planets):
        print(f'-> {planet}')
