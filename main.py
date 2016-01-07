from hero import Hero
from spell import Spell
from weapon import Weapon
from dungeons import Dungeon
from Fight import Fight


def main():
    h = Hero("Bron", "Dragonslayer", 100, 100, 2)
    w = Weapon("The Axe of Destiny", 20)
    h.equip(w)
    s = Spell("Fireball", 20, 50, 2)
    h.learn(s)
    map = Dungeon("map.txt")
    map.open_map()
    map.spawn(h)
    map.move_hero("right")
    map.move_hero("down")
    map.move_hero("down")
    map.move_hero("down")
    map.print_map()
    fight = Fight(map, h)
    print(fight.hero_attack(by="spell"))
    map.respawn()
    map.print_map()

if __name__ == '__main__':
    main()

