items = input().split("|")
budget = float(input())

new_prices = []
profit = 0
after_sale = 0

for i in items:
    crnt_item = i.split("->")
    item_price = float(crnt_item[1])
    if ((crnt_item[0] == "Clothes" and item_price <= 50) or \
        (crnt_item[0] == "Shoes" and item_price <= 35) or \
        (crnt_item[0] == "Accessories" and item_price <= 20.50)) and \
        budget >= item_price:
        budget -= item_price
        new_prices.append(item_price * 1.4)
        after_sale += item_price * 1.4
        profit += item_price * 0.4

for i in new_prices:
    if i == new_prices[-1]:
        print(f"{i:.2f}")
        break
    print(f"{i:.2f}", end= " ")

print(f"Profit: {profit:.2f}")
if after_sale + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
