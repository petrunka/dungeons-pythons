class Enemy:

    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage

    def is_alive(self):
        if self.health == 0:
            raise "The Enemy died!!!"
            return False
        raise "The Enemy is still alive"
        return True

    def can_cast(self, spellObj):
        if spellObj.mana > self.mana:
            return False
        return True

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        if self.is_alive():
            self.health += healing_points
            if self.health > 100:
                self.health == 100
        return self.is_alive()

    def take_mana(self, mana_points):
        pass

    def take_damage(self, objHero):
        self.health -= objHero.get_damage()

    def spell(self, objSpell):
        self.damage += objSpell.get_damage()

    def equip(self, objWeapon):
        self.damage += objWeapon.get_damage()

    def attack(self):
        return self.damage




