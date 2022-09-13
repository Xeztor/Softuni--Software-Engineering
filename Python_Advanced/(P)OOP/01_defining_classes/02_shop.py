class Shop:
    def __init__(self, shop_name, items):
        self.name = shop_name
        self.items = items

    def get_items_count(self):
        return len(self.items)


# shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
# print(shop.get_items_count())
