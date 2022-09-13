from collections import deque
import typing

BOMB_REQUIREMENTS = {'cherry_bomb': 60, 'datura_bomb': 40, 'smoke_decoy_bomb': 120}


def is_pouch_full(pouch_to_check):
    for bomb_type, quantity in pouch_to_check.items():
        if not quantity >= 3:
            return False
    return True


def what_bomb_is_this_val(bomb_val):
    if bomb_val == BOMB_REQUIREMENTS['cherry_bomb']:
        return 'cherry_bomb'
    elif bomb_val == BOMB_REQUIREMENTS['datura_bomb']:
        return 'datura_bomb'
    elif bomb_val == BOMB_REQUIREMENTS['smoke_decoy_bomb']:
        return 'smoke_decoy_bomb'


def print_bomb_effects(bombs):
    if bombs:
        print(f"Bomb Effects: {', '.join(map(str, bombs))}")
    else:
        print('Bomb Effects: empty')


def print_casings(casings_l):
    if casings_l:
        print(f"Bomb Casings: {', '.join(map(str, casings_l))}")
    else:
        print('Bomb Casings: empty')


def print_pouch(pouch_d):
    print(f"Cherry Bombs: {pouch_d['cherry_bomb']}")
    print(f"Datura Bombs: {pouch_d['datura_bomb']}")
    print(f"Smoke Decoy Bombs: {pouch_d['smoke_decoy_bomb']}")


bomb_effects = deque(map(int, input().split(', ')))
casings = list(map(int, input().split(',')))

pouch = {'cherry_bomb': 0, 'datura_bomb': 0, 'smoke_decoy_bomb': 0}


while bomb_effects and casings:
    if is_pouch_full(pouch):
        print('Bene! You have successfully filled the bomb pouch!')
        break

    bomb_comb_val = bomb_effects[0] + casings[-1]

    check = what_bomb_is_this_val(bomb_comb_val)

    if check:
        pouch[check] += 1
        bomb_effects.popleft()
        casings.pop()
    else:
        casings[-1] -= 5

if not is_pouch_full(pouch):
    print("You don't have enough materials to fill the bomb pouch.")

print_bomb_effects(bomb_effects)
print_casings(casings)
print_pouch(pouch)