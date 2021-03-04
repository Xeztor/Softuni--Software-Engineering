class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

        self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= ingredient_price * quantity

    def make_order(self):
        ingredients = self.get_ingredients()
        PizzaDelivery.ordered = True
        return f"You've ordered pizza {self.name} prepared with " + \
               ', '.join(ingredients) + f" and the price will be {self.price}lv."

    def get_ingredients(self):
        ingredients = []
        for ingredient, qty in self.ingredients.items():
            ingredients.append(f"{ingredient}: {qty}")
        return ingredients


# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))
