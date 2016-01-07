from treasures import Treasures


class Dungeon:

    def __init__(self, map_name):
        self.map = []
        self.map_name = map_name
        self.coords = [0, 0]
        # self.hero = None

    def get_coords(self):
        return self.coords

    def get_coords(self):
        return self.coords
    
    def get_enemy_coords(self):
        return self.enemy_coords

    def open_map(self):
        data = open(self.map_name, 'r')
        for i in [line.split() for line in data]:
            self.map.append(i)
        data.close()

    def print_map(self):
        print(self.map)

    def get_map(self):
        return self.map

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
        return False

    def respawn(self):
        for point in range(self.coords[1], len(self.map[self.coords[0]][0])):
            if self.map[self.coords[0]][0][point] == ".":
                row = self.map[self.coords[0]][0].replace("H", ".")
                l = list(row)
                l[point] = "H"
                row = "".join(l)
                self.map[self.coords[0]].remove(self.map[self.coords[0]][0])
                self.map[self.coords[0]].append(row)
                return "Hero respawned"

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
            if self.check_move('down', el, current_row, index):
                self.move_down(el, current_row, index)
                return True
        return False
<<<<<<< HEAD


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

=======
>>>>>>> 3636551c1a01618945e8f0e05787da3ef65cf189
