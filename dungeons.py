class Dungeon:

    def __init__(self):
        self.map = []

    def print_map(self):
        data = open('map.txt', 'r')
        new_data = []
        new_data = [line.split() for line in data]
        for i in new_data:
            self.map.append(i)
        print(self.map)
        data.close()

    def spawn(self, hero)

def main():
    d = Dungeon()
    d.print_map()

if __name__ == '__main__':
    main()

