from hero import Hero
from treasures import Treasures
from spell import Spell
from weapon import Weapon
from enemy import Enemy


class Dungeon:

    def __init__(self, map_name):
        self.map = []
        self.map_name = map_name
        self.coords = []
        self.hero = None
        self.enemy_coords = []
        self.enemy = None

    def open_map(self):
        data = open(self.map_name, 'r')
        for i in [line.split() for line in data]:
            self.map.append(i)
        data.close()

    def print_map(self):
        print(self.map)

    def spawn(self, hero):
        self.hero = hero
        for el in self.map:
            for i in range(0, len(el)):
                        if 'S' in el[i]:
                            row = el[i]
                            new_i = el[i].replace('S', 'H')
                            self.coords.append(i)
                            self.coords.append(el[i].index("S"))
                            el.remove(row)
                            el.append(new_i)
                            return True
        if self.hero.health == 0:
            self.respawn()
        return False

    def respawn(self):
        pass

    def move_right(self, el, current_row, index):
        new_position = current_row[:index] + '.' + 'H' + current_row[index+2:]
        self.map[el].remove(self.map[el][0])
        self.map[el].append(new_position)
        self.coords = []
        self.coords.append(el)
        self.coords.append(new_position.index("H"))

    def move_left(self, el, current_row, index):
        new_position = current_row[:index-1] + 'H' + '.' + current_row[index+1:]
        self.map[el].remove(self.map[el][0])
        self.map[el].append(new_position)
        self.coords = []
        self.coords.append(el)
        self.coords.append(new_position.index("H"))

    def move_up(self, el, current_row, index):
        new_row = self.map[el - 1]
        self.replace(current_row, el, index, new_row)

    def move_down(self, el, current_row, index):
        new_row = self.map[el + 1]
        self.replace(current_row, el, index, new_row)

    def replace(self, current_row, el, index, new_row):
        new_position = new_row[0][:index] + 'H' + new_row[0][index+1:]
        new_row.append(new_position)
        new_row.remove(new_row[0])
        reload_poins = current_row.replace('H', '.')
        self.map[el].append(reload_poins)
        self.map[el].remove(current_row)
        self.coords = []
        self.coords.append(self.map.index(new_row))
        self.coords.append(new_position.index("H"))

    def cases(self, current_point):
        if current_point == '.':
            return True
        if current_point == 'E':
            pass
        if current_point == 'T':
            print(Treasures.pick_treasure())
            return True
        if current_point == '#':
            return False
        if current_point == 'G':
            print("End of dungeon!!!")

    def check_move(self, move, el, current_row, index):
        if move == 'right':
            if index < len(current_row)-1:
                current_point = self.map[el][0][index+1]
                return(self.cases(current_point))
            return False
        if move == 'left':
            if index >= 1 and index < len(current_row):
                current_point = self.map[el][0][index-1]
                return(self.cases(current_point))
            return False
        if move == 'up':
            if index >= 0:
                current_point = self.map[el - 1][0][index]
                return(self.cases(current_point))
            return False
        if move == 'down':
            if index < len(self.map):
                # print(el)
                current_point = self.map[el + 1][0][index]
                return(self.cases(current_point))
            return False

    def move_hero(self, direction):
        el = self.coords[0]
        print(el)
        current_row = (self.map[el][0])
        index = self.coords[1]
        if direction == 'right':
            if self.check_move('right', el, current_row, index):
                self.move_right(el, current_row, index)
                return True
        if direction == 'left':
            if self.check_move('left', el, current_row, index):
                self.move_left(el, current_row, index)
                return True
        if direction == 'up':
            if self.check_move('up', el, current_row, index):
                self.move_up(el, current_row, index)
                return True
        if direction == 'down':
            # print(el)
            if self.check_move('down', el, current_row, index):
                self.move_down(el, current_row, index)
                return True
        return False

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
            self.start_fight_by_weapon()

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

    def hero_attack(self, by="spell"):
        if self.hero.spell.damage >= self.hero.weapon.damage:
            if self.check_range_attack():
                self.enemy = Enemy(100, 100, 20)
                print(self.message_start_fight())
                self.start_fight_by_spell()
            else:
                return "Nothing in casting range " + str(self.hero.spell.cast_range)
        else:
            self.start_fight_by_weapon()

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


def main():
    h = Hero("Bron", "Dragonslayer", 100, 100, 2)
    w = Weapon("The Axe of Destiny", 20)
    h.equip(w)
    s = Spell("Fireball", 20, 50, 2)
    h.learn(s)
    map = Dungeon("map.txt")
    map.open_map()
    map.spawn(h)
    print(map.move_hero("right"))
    print(map.move_hero("down"))
    print(map.move_hero("down"))
    map.print_map()
    print(map.hero_attack(by="spell"))

if __name__ == '__main__':
    main()

