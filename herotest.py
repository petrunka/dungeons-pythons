from weapon import Weapon
from spell import Spell
from hero import Hero
import unittest

class HeroTest(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("Batman", "Superman", 200, 105, 15)
        self.weapon = Weapon("pistol", 45)
        self.spell = Spell("Abracadabra", 35, 40, 11)

    def test_init(self):
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()
        
