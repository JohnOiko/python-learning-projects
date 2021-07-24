from random import randrange


# class that represents a generic character
class Character:
    def __init__(self, character_name, equipment, attack_speed, delay, max_health=100, max_delay=5, attack_range=(3, 11)):
        self.character_name = character_name.capitalize()
        self.equipment = equipment
        self.max_health = max_health * self.equipment.cape
        self.health = self.max_health
        self.attack_speed = attack_speed
        self.delay = delay
        self.max_delay = max_delay
        self.attack_range = attack_range

    def attack(self):
        self.delay = self.max_delay - self.attack_speed
        return round(randrange(self.attack_range[0], self.attack_range[1]) * self.equipment.sword)

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
