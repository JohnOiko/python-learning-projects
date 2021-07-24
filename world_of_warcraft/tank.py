from character import Character


# class that represents a tank character
class Tank(Character):
    def __init__(self, character_name, equipment, attack_speed, delay, max_health=200, max_delay=5, attack_range=(20, 30)):
        super().__init__(character_name, equipment, attack_speed, delay, max_health, max_delay, attack_range)