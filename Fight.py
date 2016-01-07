from enemy import Enemy


class Fight:

    def __init__(self, dungeon, hero):
        self.dungeon = dungeon
        self.hero = hero
        self.coords = dungeon.get_coords()
        self.map = dungeon.map
        self.enemy_coords = []
        self.enemy = None

    def message_start_fight(self):
        return "A fight is started between our {} and {}".format(self.hero, self.enemy)

    def message_hero_cast(self):
        return "Hero casts a {}, hits enemy for {}dmg.Enemy health is {} \
        ".format(self.hero.spell.name, self.hero.spell.damage, self.enemy.health)

    def message_no_more_mana(self):
        return "Hero does not have mana for another {}.".format(self.hero.spell.name)

    def message_enemy_hit(self):
        return "Enemy hits hero with {}dmg. Hero health is {}".format(self.enemy.damage, self.hero.health)

    def message_move_enemy(self):
        return "Enemy moves one square to the {} in order to get to the hero. This is his move.".format(self.give_moved_direction())

    def message_use_weapon(self):
        return "Hero hits with {} for {} dmg. Enemy health is {}".format(self.hero.weapon.name, self.hero.weapon.damage, self.enemy.health)

    def message_dead(self, dead):
        return "{} is dead!".format(dead)

    def give_moved_direction(self):
        if self.coords[0] > self.enemy_coords[0]:
            return "up"
        if self.coords[0] < self.enemy_coords[0]:
            return "down"
        if self.coords[1] > self.enemy_coords[1]:
            return "right"
        else:
            return "left"

    def move_enemy(self, direction):
        if direction == "right":
            self.enemy_coords[1] += 1
            return
        if direction == "left":
            self.enemy_coords[1] -= 1
            return
        if direction == "up":
            self.enemy_coords[0] -= 1
            return
        else:
            self.enemy_coords[0] += 1
            return

    def different_positions(self):
        return self.coords == self.enemy_coords

    def start_fight_by_spell(self):
            while self.hero.curr_mana > 0:
                self.enemy.health -= self.hero.damage
                print(self.message_hero_cast())
                if not self.different_positions():
                    print(self.message_move_enemy())
                    self.move_enemy(self.give_moved_direction())
                else:
                    self.hero.health -= self.enemy.damage
                    print(self.message_enemy_hit())
                self.hero.curr_mana -= self.hero.spell.mana_cost
            print(self.message_no_more_mana())
            return self.start_fight_by_weapon()

    def start_fight_by_weapon(self):
        while self.hero.health and self.enemy.health > 0:
            self.enemy.health -= self.hero.weapon.damage
            print(self.message_use_weapon())
            self.hero.health -= self.enemy.damage
            print(self.message_enemy_hit())
        if self.hero.health == 0:
            print(self.message_dead(self.hero.name))
        if self.enemy.health == 0:
            print(self.message_dead("Enemy"))
        return

    def hero_attack(self, by="spell"):
        if self.hero.spell.damage >= self.hero.weapon.damage:
            if self.check_range_attack():
                self.enemy = Enemy(100, 100, 20)
                print(self.message_start_fight())
                return self.start_fight_by_spell()
            else:
                return "Nothing in casting range " + str(self.hero.spell.cast_range)
        else:
            return self.start_fight_by_weapon()

    def check_range_attack(self):
        dy = self.coords[0]
        dx = self.coords[1]
        cast_range = self.hero.spell.cast_range
        left_index = dx - cast_range
        right_index = dx + cast_range
        up_index = dy - cast_range
        down_index = dy + cast_range

        if left_index or up_index < 0:
            left_index, up_index = 0, 0
        if right_index >= len(self.map[dx][0]):
            right_index = len(self.map[dx][0]) - 1
        if down_index >= len(self.map):
            down_index = len(self.map) - 1

        for i in range(left_index, right_index):
            for j in range(up_index, down_index):
                if self.map[j][0][i] == "E":
                    self.enemy_coords.append(j)
                    self.enemy_coords.append(i)
                    return True
        return False
