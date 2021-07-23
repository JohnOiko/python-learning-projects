from random import randrange


# class that represents a single character
class Character:
    def __init__(self, character_name, equipment, attack_speed, delay):
        self.character_name = character_name.capitalize()
        self.equipment = equipment
        self.health = 100 * self.equipment.cape
        self.max_health = 100 * self.equipment.cape
        self.attack_speed = attack_speed
        self.delay = delay

    def attack(self):
        self.delay = 5 - self.attack_speed
        return round(randrange(3, 11) * self.equipment.sword)

    def is_dead(self):
        return self.health == 0

    def end_round(self):
        if self.health < self.max_health:
            self.health += 1
        if self.delay > 0:
            self.delay -= 1

    def __str__(self):
        return f"{self.character_name}: H = {round(self.health)} D = {self.delay}"

    def __repr__(self):
        return f"Character({self.character_name}, {self.attack_speed}, {self.delay}, {round(self.health)}, " \
               f"{round(self.max_health)}, {repr(self.equipment)})"

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.health = min(self.health + other, self.max_health)
        return self

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.health = max(self.health - other, 0)
        return self
