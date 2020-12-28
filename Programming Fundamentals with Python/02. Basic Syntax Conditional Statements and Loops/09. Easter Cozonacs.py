budget = float(input())
flour_price_kg = float(input())

eggs_price = 0.75 * flour_price_kg
liter_milk = 1.25 * flour_price_kg

cozonac_price = flour_price_kg + eggs_price + liter_milk * 0.25
cozonac_count = 0

colored_eggs = 0

while budget - cozonac_price > 0:
    cozonac_count += 1
    colored_eggs += 3
    if cozonac_count % 3 == 0:
        colored_eggs -= cozonac_count - 2
    budget -= cozonac_price
print(f"You made {cozonac_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
