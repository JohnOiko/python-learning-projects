from character import Character
from arena import Arena
from random import seed, randrange
from datetime import datetime

seed(datetime.now())


def main():
    orcs = [Character("Orc", 2, randrange(4)) for _ in range(5)]
    night_elfs = [Character("Night Elf", 3, randrange(3)) for _ in range(3)]

    arena = Arena(orcs, night_elfs)
    arena.play()


main()
