from collections import deque


def is_pouch_full(pouch_to_check):
    for firework_type, quantity in pouch_to_check.items():
        if not quantity >= 3:
            return False
    return True


def what_firework_is_this_val(firework_val):
    if firework_val % 3 == 0 \
            and firework_val % 5 == 0:
        return 'crossette_firework'
    elif firework_val % 3 == 0:
        return 'palm_firework'
    elif firework_val % 5 == 0:
        return 'willow_firework'


def print_firework_efx(firework_efx):
    if firework_efx:
        print(f"Firework Effects left: {', '.join(map(str, firework_efx))}")


def print_explosive_powers(powers):
    if powers:
        print(f"Explosive Power left: {', '.join(map(str, powers))}")


def print_pouch(pouch_dict):
    print(f"Palm Fireworks: {pouch_dict['palm_firework']}")
    print(f"Willow Fireworks: {pouch_dict['willow_firework']}")
    print(f"Crossette Fireworks: {pouch_dict['crossette_firework']}")


firework_effects = deque(map(int, input().split(', ')))
explosive_powers = list(map(int, input().split(',')))

pouch = {'palm_firework': 0, 'willow_firework': 0, 'crossette_firework': 0}

while firework_effects and explosive_powers:
    if is_pouch_full(pouch):
        break

    crnt_firework_effect = firework_effects[0]
    crnt_explosive_fire = explosive_powers[-1]

    if crnt_firework_effect <= 0:
        firework_effects.popleft()
        continue
    elif crnt_explosive_fire <= 0:
        explosive_powers.pop()
        continue

    firework = what_firework_is_this_val(crnt_firework_effect + crnt_explosive_fire)

    if firework:
        pouch[firework] += 1
        firework_effects.popleft()
        explosive_powers.pop()
    else:
        crnt_firework_effect -= 1
        firework_effects.popleft()
        firework_effects.append(crnt_firework_effect)

if not is_pouch_full(pouch):
    print("Sorry. You can’t make the perfect firework show.")
else:
    print('Congrats! You made the perfect firework show!')

print_firework_efx(firework_effects)
print_explosive_powers(explosive_powers)
print_pouch(pouch)
