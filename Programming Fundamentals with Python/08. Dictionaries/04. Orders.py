product = input().split()

data_products = {}

while 'buy' not in product:
    name, price, qty = product
    if name not in data_products:
        data_products[name] = {'price': float(price), 'qty': int(qty)}
    else:
        if not data_products[name]['price'] == price:
            data_products[name]['price'] = float(price)
        data_products[name]['qty'] += int(qty)

    product = input().split()

for k, v in data_products.items():
    print(f"{k} -> {v['price'] * v['qty']:.2f}")
