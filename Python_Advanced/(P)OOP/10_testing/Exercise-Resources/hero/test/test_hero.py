import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('lazaroni', 10, 100.0, 50)

    def test_hero_battle_when_username_is_same_as_yours__expect_exception(self):
        with self.assertRaises(Exception) as exc:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(exc.exception))

    def test_hero_battle_when_your_health_is_below_or_equal_to_0__expect_exception(self):
        enemy = Hero('enemy', 10, 100.0, 50)
        self.hero.health = 0
        with self.assertRaises(Exception) as exc:
            self.hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(exc.exception))

    def test_hero_battle_when_enemy_health_is_below_or_equal_to_0__expect_exception(self):
        enemy = Hero('enemy', 10, 0.0, 50.0)
        with self.assertRaises(Exception) as exc:
            self.hero.battle(enemy)

        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(exc.exception))

    def test_hero_battle_when_your_dmg_more_than_enemy__expect_return_msg_and_changed_level_health_damage(self):
        enemy = Hero('enemy', 3, 50.0, 20.0)
        msg = self.hero.battle(enemy)
        self.assertEqual(self.hero.health, 45)
        self.assertEqual(self.hero.level, 11)
        self.assertEqual(self.hero.damage, 55)
        self.assertEqual("You win", msg)

    def test_hero_battle_when_enemy_dmg_more_than_yours__expect_return_msg_and_changed_level_health_damage_on_enemy(
            self):
        self.hero.damage = 1
        enemy = Hero('enemy', 4, 100.0, 25.0)
        msg = self.hero.battle(enemy)
        self.assertEqual(enemy.health, 95)
        self.assertEqual(enemy.level, 5)
        self.assertEqual(enemy.damage, 30)
        self.assertEqual('You lose', msg)

    def test_hero_battle_when_draw__expect_msg(self):
        enemy = Hero('enemy', 4, 100.0, 25.0)
        msg = self.hero.battle(enemy)
        self.assertEqual('Draw', msg)

    def test_hero_string_representation(self):
        actual = str(self.hero)
        self.assertEqual(
            f"Hero {self.hero.username}: {self.hero.level} lvl\n"
            f"Health: {self.hero.health}\n"
            f"Damage: {self.hero.damage}\n", actual)


if __name__ == '__main__':
    unittest.main()
