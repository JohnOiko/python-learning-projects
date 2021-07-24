from character import Character
from random import randrange


# class that represents a mage character
class Mage(Character):
    def __init__(self, character_name, equipment, attack_speed, delay, max_health=100, max_delay=5, attack_range=(8, 17), max_mana=100):
        super().__init__(character_name, equipment, attack_speed, delay, max_health, max_delay, attack_range)
        self.max_mana = max_mana
        self.mana = self.max_mana

    def lighting_spell(self):
        self.mana = max(self.mana - 55, 0)
        return round(randrange(30, 51))

    def attack(self):
        self.delay = self.max_delay - self.attack_speed
        if self.mana >= 55:
            return self.lighting_spell()
        else:
            return round(randrange(self.attack_range[0], self.attack_range[1]) * self.equipment.sword)

    def end_round(self):
        super().end_round()
        if self.mana < self.max_mana:
            self.mana += 1
