from collections import OrderedDict, defaultdict
import re
products = OrderedDict()
qty = defaultdict(int)
n = int(input())

for _ in range(n):
    product = input()
    item_name, price = re.search(r'(?P<name>[^0-9]+)\s+(?P<price>\d+)', product).group('name', 'price')
    products[item_name] = int(price)
    qty[item_name] += 1

for item, price in products.items():
    print(f'{item} {price * qty[item]}')
