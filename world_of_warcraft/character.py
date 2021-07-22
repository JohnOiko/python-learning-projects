from random import randrange


# class that represents a single character
class Character:
    def __init__(self, name, attack_speed, delay):
        self.name = name.capitalize()
        self.health = 100
        self.attack_speed = attack_speed
        self.delay = delay

    def attack(self):
        self.delay = 5 - self.attack_speed
        return randrange(3, 11)

    def is_dead(self):
        return self.health == 0

    def end_round(self):
        if self.health < 100:
            self.health += 1
        if self.delay > 0:
            self.delay -= 1

    def print(self):
        print(f"{self.name}:\n\tH = {self.health}\n\tAS = {self.attack_speed}\n\tD = {self.delay}")
