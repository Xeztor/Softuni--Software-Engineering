quantity = int(input())
days_left = int(input())

ornament_set = 2
tree_skirt = 5
tree_gerland = 3
lights = 15

spent = 0
spirit = 0
days_past = 1

while days_past != days_left:
    days_past += 1
    if days_past % 11 == 0:
        quantity += 2
    if days_past % 2 == 0:
        spent += ornament_set * quantity
        spirit += 5
    if days_past % 3 == 0:
        spent += (tree_skirt + tree_gerland) * quantity
        spirit += 13
    if days_past % 5 == 0:
        spent += lights * quantity
        spirit += 17
        if days_past % 3 == 0:
            spirit += 30
    if days_past % 10 == 0:
        spent += tree_skirt + tree_gerland + lights
        spirit -= 20

    if days_past % 10 == 0 and days_past == days_left:
        spirit -= 30

print(f"Total cost: {spent}")
print(f"Total spirit: {spirit}")
