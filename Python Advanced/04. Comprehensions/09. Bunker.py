categories = {category_name: {} for category_name in input().split(', ')}

n = int(input())

for _ in range(n):
    category, item, quality_quantity = input().split(' - ')
    quantity, quality = quality_quantity.split(';')
    quantity = int(quantity.split(':')[1])
    quality = int(quality.split(':')[1])
    categories[category][item] = {'quantity': quantity, 'quality': quality}

all_items = 0
avarage = 0
for category, items in categories.items():
    all_items += sum([stats['quantity'] for item_name, stats in items.items()])
    avarage += sum([stats['quality'] for item_name, stats in items.items()])

print(f'Count of items: {all_items}')
print(f'Average quality: {avarage / len(categories):.2f}')
for category, items in categories.items():
    print(f"{category} -> {', '.join([item for item in items])}")
