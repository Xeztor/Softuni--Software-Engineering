def battle_ships(rows, attacks):
    ships_destroyed = 0
    for i in range(len(attacks)):
        crnt_attack = attacks[i]
        crnt_attack = crnt_attack.split("-")
        attack_row, attack_column = list(map(int, crnt_attack))
        crnt_row = rows[attack_row]
        crnt_row = crnt_row.split()
        crnt_row = list(map(int, crnt_row))
        if crnt_row[attack_column] - 1 == 0:
            ships_destroyed += 1
            crnt_row[attack_column] = 0
            rows[attack_row] = " ".join(list(map(str, crnt_row)))
        elif crnt_row[attack_column] > 1:
            crnt_row[attack_column] -= 1
            rows[attack_row] = " ".join(list(map(str, crnt_row)))
    return ships_destroyed


n = int(input())

rows_given = []
for i in range(n):
    rows_given.append(input())

attack_given = input().split()

print(battle_ships(rows_given, attack_given))
