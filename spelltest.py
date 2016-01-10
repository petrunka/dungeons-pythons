from spell import Spell
import unittest

class WeaponTest(unittest.TestCase):
    def setUp(self):
        self.spell = Spell("Abracadabra", 100, 11, 15)

    def test_damage(self):
        self.assertEqual(self.spell.get_damage(), 100)

    def test_name(self):
        self.assertEqual(self.spell.get_name(), 'Abracadabra')

    def test_mana_cost(self):
        self.assertEqual(self.spell.get_mana_cost(), 11)

    def test_cast_range(self):
        self.assertEqual(self.spell.get_cast_range(), 15)

if __name__ == "__main__":
        unittest.main()
