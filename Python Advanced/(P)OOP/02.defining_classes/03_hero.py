class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage_dealt):
        if self.health <= damage_dealt:
            self.health = 0
            return f'{self.name} was defeated'
        else:
            self.health -= damage_dealt

    def heal(self, health_points):
        self.health += health_points


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))

