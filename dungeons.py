from hero import Hero
from treasures import Treasures
from spell import Spell
from weapon import Weapon
from enemy import Enemy


class Dungeon:

    def __init__(self, map_name):
        self.map = []
        self.map_name = map_name

    def open_map(self):
        data = open(self.map_name, 'r')
        for i in [line.split() for line in data]:
            self.map.append(i)
        data.close()

    def print_map(self):
        print(self.map)

    def spawn(self, hero):
        for el in self.map:
            for i in range(0, len(el)):
                        if 'S' in el[i]:
                            row = el[i]
                            new_i = el[i].replace('S', 'H')
                            el.remove(row)
                            el.append(new_i)
                            return True
        # if not hero.is_alive():
        #     flag = 0
        #     for el in self.map:
        #         for i in range(0, len(el)):
        #             if el[i] == 'S' and flag == 0:
        #                 el[i] = 'H'
        #                 flag = 1
        return False

    def find_coordinates(self):
        for row in self.map:
            for i in range(0, len(row)):
                if 'H' in row[i]:
                    list_coordinates = []
                    list_coordinates.append(self.map.index(row))
                    list_coordinates.append(row[i].index('H'))
                    return list_coordinates

    def move_right(self, el, current_row, index):
        new_position = current_row[:index] + '.' + 'H' + current_row[index+2:]
        self.map[el].remove(self.map[el][0])
        self.map[el].append(new_position)

    def move_left(self, el, current_row, index):
        new_position = current_row[:index-1] + 'H' + '.' + current_row[index+1:]
        self.map[el].remove(self.map[el][0])
        self.map[el].append(new_position)

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
                current_point = self.map[el + 1][0][index]
                return(self.cases(current_point))
            return False

    def move_hero(self, direction):
        el = self.find_coordinates()[0]
        current_row = (self.map[el][0])
        index = self.find_coordinates()[1]
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
            if self.check_move('down', el, current_row, index):
                self.move_down(el, current_row, index)
                return True
        return False

    def hero_attack(self, by="spell"):
        if Weapon.damage > Spell.damage:
            Hero.damage = Weapon.damage
        Spell.cast_range -= 1
        Enemy.health -= Hero.damage


def main():
    # d = Dungeon("map.txt")
    # d.open_map()
    # d.print_map()
    # hero = Hero("Bron", "Dragonslayer", 100, 100, 2)
    # d.spawn(hero)
    # d.print_map()
    # print(d.move_hero("right"))
    # d.print_map()
    # # print(d.move_hero("right"))
    # # d.print_map()
    # # print(d.move_hero("left"))
    # # d.print_map()
    # print(d.move_hero("down"))
    # d.print_map()
    # print(d.move_hero("up"))
    # d.print_map()
    # print(d.move_hero("up"))
    # d.print_map()
    h = Hero("Bron", "Dragonslayer", 100, 100, 2)
    w = Weapon("The Axe of Destiny", 20)
    h.equip(w)
    s = Spell("Fireball", 30, 50, 2)
    h.learn(s)
    map = Dungeon("map.txt")
    map.open_map()
    map.spawn(h)
    map.print_map()
    print(map.move_hero("right"))
    print(map.move_hero("down"))
    map.print_map()
    e = Enemy(100, 100, 20)
    map.hero_attack(by="spell")
    print(e.health)

if __name__ == '__main__':
    main()

