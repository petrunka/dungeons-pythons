from hero import Hero
from treasures import Treasures
from spell import Spell
from weapon import Weapon
from enemy import Enemy
from dungeons import Dungeon

class Fight:

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        self.dungeon = Dungeon("Treasure-Map")

    def message_start_fight(self):
        return "A fight is started between our {} and {}".format(self.hero, self.enemy)

    def message_hero_cast(self):
        return "Hero casts a {}, hits enemy for {} dmg.Enemy health is {} \
        ".format(self.hero.get_spell().get_name(), self.hero.get_spell().get_damage(), self.enemy.get_health())

    def message_no_more_mana(self):
        return "Hero does not have mana for another {}.".format(self.hero.get_spell().get_name())

    def message_enemy_hit(self):
        return "Enemy hits hero with {}dmg. Hero health is {}".format(self.enemy.get_damage(), self.hero.get_health())

    def message_move_enemy(self):
        return "Enemy moves one square to the {} in order to get to the hero. This is his move.".format(self.dungeon.give_moved_direction())

    def message_use_weapon(self):
        return "Hero hits with {} for {} dmg. Enemy health is {}".format(self.hero.get_weapon().get_name(), self.hero.get_weapon().get_damage(), self.enemy.get_health())

    def message_dead(self, dead):
        return "{} is dead!".format(dead)

    def give_moved_direction(self):
        if self.dungeon.get_coords()[0] > self.dungeon.get_enemy_coords()[0]:
            return "up"
        if self.dungeon.get_coords()[0] < self.dungeon.get_enemy_coords()[0]:
            return "down"
        if self.dungeon.get_coords()[1] > self.dungeon.get_enemy_coords()[1]:
            return "right"
        else:
            return "left"

    def move_enemy(self, direction):
        if direction == "right":
            self.dungeon.get_enemy_coords()[1] += 1
            return
        if direction == "left":
            self.dungeon.get_enemy_coords()[1] -= 1
            return
        if direction == "up":
            self.dungeon.get_enemy_coords()[0] -= 1
            return
        else:
            self.dungeon.get_enemy_coords()[0] += 1
            return

    def different_positions(self):
        return self.dungeon.get_coords() == self.dungeon.get_enemy_coords()

    def start_fight_by_spell(self):
            while self.hero.get_mana() > 0:
                self.enemy.get_health() -= self.hero.get_damage()
                print(self.message_hero_cast())
                if not self.different_positions():
                    print(self.message_move_enemy())
                    self.move_enemy(self.give_moved_direction())
                else:
                    self.hero.get_health() -= self.enemy.get_damage()
                    print(self.message_enemy_hit())
                self.hero.get_mana() -= self.hero.get_spell().get_mana_cost()
            print(self.message_no_more_mana())
            self.start_fight_by_weapon()

    def start_fight_by_weapon(self):
        while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
            self.enemy.get_health() -= self.hero.get_weapon().get_damage()
            print(self.message_use_weapon())
            self.hero.get_health() -= self.enemy.get_damage()
            print(self.message_enemy_hit())
        if self.hero.get_health() == 0:
            print(self.message_dead(self.hero.get_name()))
        if self.enemy.get_health() == 0:
            print(self.message_dead("Enemy"))

    def hero_attack(self, by="spell"):
        if self.hero.get_spell().get_damage() >= self.hero.get_weapon().get_damage():
            if self.check_range_attack():
                self.enemy = Enemy(100, 100, 20)
                print(self.message_start_fight())
                self.start_fight_by_spell()
            else:
                return "Nothing in casting range " + str(self.hero.get_spell().get_cast_range())
        else:
            self.start_fight_by_weapon()

    def check_range_attack(self):
        dy = self.dungeon.get_coords()[0]
        dx = self.dungeon.get_coords()[1]
        cast_range = self.hero.get_spell().get_cast_range()
        left_index = dx - cast_range
        right_index = dx + cast_range
        up_index = dy - cast_range
        down_index = dy + cast_range

        if left_index or up_index < 0:
            left_index, up_index = 0, 0
        if right_index >= len(self.dungeon.get_map()[dx][0]):
            right_index = len(self.dungeon.get_map()[dx][0]) - 1
        if down_index >= len(self.dungeon.get_map()):
            down_index = len(self.dungeon.get_map()) - 1

        for i in range(left_index, right_index):
            for j in range(up_index, down_index):
                if self.dungeon.get_map()[j][0][i] == "E":
                    self.dungeon.get_enemy_coords().append(j)
                    self.dungeon.get_enemy_coords().append(i)
                    return True
        return False
