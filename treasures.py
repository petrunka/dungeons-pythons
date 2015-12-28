import random


class Treasures:

    @staticmethod
    def pick_treasure():
        dice = random.choice(['mana', 'health potion', 'spell', 'weapon'])
        if dice == 'health potion':
            return "Found " + dice + ". Health is max"
        return "Found " + dice

