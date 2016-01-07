class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.curr_health = health
        self.damage = 0
        self.curr_mana = mana
        self.max_mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.spell = None
        self.weapon = None

    def get_name(self):
        return self.name

    def __str__(self):
        return "{} {} with health {}, mana {} and damage {}".format(self.name, self.title, self.curr_health, self.curr_mana, self.damage)

    def __repr__(self):
        return self.__str__()

    def known_as(self):
        return "{} {}".format(self.name, self.title)

    def get_health(self):
        return self.curr_health

    def get_mana(self):
        return self.curr_mana

    def get_weapon(self):
        return self.weapon

    def get_spell(self):
        return self.spell

    def set_position(self):
        pass

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def can_cast(self, other):
        if self.mana > other.mana:
            return True
        else:
            return False

    def take_damage(self, damage_points):
        if self.curr_health > damage_points:
            self.curr_health -= damage_points
        else:
            self.curr_health = 0

    def take_healing(self, healing_points):
        if self.curr_health == 0:
            raise Exception
        elif self.curr_health + healing_points > self.max_health:
            self.curr_health = self.max_health
        else:
            self.curr_health += healing_points

    def take_mana(self, mana_points):
        if self.curr_mana + mana_points > self.max_mana:
            self.curr_mana = self.max_mana
        else:
            self.curr_mana += mana_points

    def equip(self, weapon):
        self.damage = weapon.get_damage()
        self.weapon = weapon

    def get_damage(self):
        return self.damage

    def learn(self, spell):
        self.damage = spell.get_damage()
        self.spell = spell

    def attack(self, by="weapon"):
        return "{}".format(by).get_damage()
