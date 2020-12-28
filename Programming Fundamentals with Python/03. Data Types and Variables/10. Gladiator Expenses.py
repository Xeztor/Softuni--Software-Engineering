lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
broken_shields = 0

for i in range(1, lost_fights +1):

    if i % 2 == 0:
        expenses += helmet_price
        if i % 3 == 0:
            expenses += sword_price
            expenses += shield_price
            broken_shields += 1
    elif i % 3 == 0:
        expenses += sword_price
    if broken_shields == 2:
        broken_shields = 0
        expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
