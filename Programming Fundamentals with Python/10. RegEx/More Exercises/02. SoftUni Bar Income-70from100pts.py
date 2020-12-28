import re
pattern = r'^%(?P<customer>[A-Z][a-z]+)%([^\|\$\.%]+)?<(?P<product>[A-Z][a-z]+)>([^\|\$\.%]+)?\|(?P<qty>\d+)\|([^\|\$\.%0-9]+)?(?P<price>\d+(\.\d+)?)\$$'

total_income = 0

client_order = input()
while not client_order == 'end of shift':
    if re.match(pattern, client_order):
        order_data = re.search(pattern, client_order)
        customer, product, qty, price = order_data.group('customer', 'product', 'qty', 'price')
        print(f'{customer}: {product} - {float(price) * int(qty):.2f}')
        total_income += float(price) * int(qty)

    client_order = input()

print(f'Total income: {total_income:.2f}')
