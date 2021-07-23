from equipment import Equipment
from character import Character
from arena import Arena
from random import seed, randrange, uniform
from datetime import datetime


def main():
    seed(datetime.now())

    orcs = [Character(f"Orc {i + 1}", Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 2, randrange(4)) for i in range(5)]
    night_elfs = [Character(f"Night Elf {i + 1}", Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 3, randrange(3)) for i in range(3)]

    arena = Arena(orcs, night_elfs)
    arena.play()


main()
