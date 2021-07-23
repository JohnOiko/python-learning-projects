from character import Character
from random import choice


# class that represents a single character
class Arena:
    def __init__(self, team_a, team_b):
        self.team_A = team_a
        self.team_B = team_b

    # method that has characters from enemy teams attack each other until only one team is left standing
    def play(self):
        print(f"{'=' * 60}")
        turn_counter = 0
        while True:

            turn_counter += 1
            print(f"Turn {turn_counter}\n")
            print(self)

            available_characters = []
            for character in self.team_A:
                if character.delay == 0:
                    available_characters.append([character, "A"])

            for character in self.team_B:
                if character.delay == 0:
                    available_characters.append([character, "B"])

            for attacker in available_characters:
                damage = attacker[0].attack()
                if attacker[1] == "A":
                    defender = [choice(self.team_B), "B"]
                    defender[0] -= damage
                else:
                    defender = [choice(self.team_A), "A"]
                    defender[0] -= damage

                print(f"{attacker[0].character_name} (team {attacker[1]}) dealt {damage} damage to {defender[0].character_name} (team {defender[1]})")

            for i in range(len(self.team_A) - 1, -1, -1):
                if self.team_A[i].is_dead():
                    print(f"{self.team_A[i].character_name} (team A) is dead!")
                    self.team_A.remove(self.team_A[i])

            for i in range(len(self.team_B) - 1, -1, -1):
                if self.team_B[i].is_dead():
                    print(f"{self.team_B[i].character_name} (team B) is dead!")
                    self.team_B.remove(self.team_B[i])

            if len(self.team_A) == 0:
                print(f"{'=' * 60}")
                print(f"Final turn ({turn_counter}) results\n")
                print(self)
                print(f"{'=' * 60}\n")
                print("Winner is team B!\n")
                print(f"{'=' * 60}")
                return
            elif len(self.team_B) == 0:
                print(f"{'=' * 60}")
                print(f"Final turn ({turn_counter}) results\n")
                print(self)
                print(f"{'=' * 60}\n")
                print("Winner is team A!\n")
                print(f"{'=' * 60}")
                return

            for character in self.team_A + self.team_B:
                character.end_round()

            print(f"{'=' * 60}")

    def __str__(self):
        string = "Team A:"
        for character in self.team_A:
            string += f"\n\t-{character}"
        string += "\n\nTeam B:"
        for character in self.team_B:
            string += f"\n\t-{character}"
        if len(self.team_B) > 0:
            string += "\n"
        return string

    def __repr__(self):
        return f"Arena([{', '.join([repr(character) for character in self.team_A])}], " \
               f"[{', '.join([repr(character) for character in self.team_B])}])"
