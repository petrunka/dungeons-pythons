from hero import Hero

class Dungeon:

    def __init__(self, map_name):
        self.map = []
        self.map_name = map_name

    def open_map(self):
        data = open(self.map_name, 'r')
        new_data = []
        new_data = [line.split() for line in data]
        for i in new_data:
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

        # if not hero.is_alive():
        #     flag = 0
        #     for el in self.map:
        #         for i in range(0, len(el)):
        #             if el[i] == 'S' and flag == 0:
        #                 el[i] = 'H'
        #                 flag = 1

    def find_coordinates(self):
        for el in self.map:
            for i in range(0, len(el)):
                if 'H' in el[i]:
                    list_coordinates = []
                    list_coordinates.append(self.map.index(el))
                    list_coordinates.append(el[i].index('H'))
                    return list_coordinates

    def move_right(self, el, current_row, index):
        new_position = current_row[:index] + '.' + 'H' + current_row[index+2:]
        self.map[el].remove(self.map[el][0])
        self.map[el].append(new_position)

    def check_move(self, move, el, current_row, index):
        if move == "right":
            if index < len(current_row):
                current_point = self.map[el][0][index+1]
                if current_point == '.':
                    self.move_right(el, current_row, index)
                if current_point == 'E':
                    pass
                if current_point == 'T':
                    pass
                if current_point == '#':
                    return False
                if current_point == 'G':
                    pass
            return False

    def move_hero(self, direction):
        el = self.find_coordinates()[0]
        current_row = (self.map[el][0])
        index = self.find_coordinates()[1]
        if direction == "right":
            self.check_move("right", el, current_row, index)
            self.move_right(el, current_row, index)


def main():
    d = Dungeon("map.txt")
    d.open_map()
    d.print_map()
    hero = Hero("Bron", "Dragonslayer", 100, 100, 2)
    d.spawn(hero)
    d.print_map()
    d.move_hero("right")
    d.print_map()
    print("helooooooooo")

if __name__ == '__main__':
    main()

