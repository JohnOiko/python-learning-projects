from character import Character
from random import choice


# class that represents a single character
class Arena:
    def __init__(self, team_a, team_b):
        self.team_A = team_a
        self.team_B = team_b

    # method that prints each team's characters
    def print_state(self):
        print(f"Team A:")
        for character in self.team_A:
            print("-", end="")
            character.print()

        print(f"\nTeam B:")
        for character in self.team_B:
            print("-", end="")
            character.print()

        print()

    # method that has characters from enemy teams attack each other until only one team is left standing
    def play(self):
        turn_counter = 0
        while True:

            turn_counter += 1
            print(f"Turn {turn_counter} start\n")
            self.print_state()

            available_characters = []
            for character in self.team_A:
                if character.delay == 0:
                    available_characters.append((character, "A"))

            for character in self.team_B:
                if character.delay == 0:
                    available_characters.append((character, "B"))

            for attacker in available_characters:
                if attacker[1] == "A":
                    defender = choice(self.team_B)
                    defender.health = max(defender.health - attacker[0].attack(), 0)
                    if defender.is_dead():
                        self.team_B.remove(defender)
                        if (defender, "B") in available_characters:
                            available_characters.remove((defender, "B"))
                else:
                    defender = choice(self.team_A)
                    defender.health = max(defender.health - attacker[0].attack(), 0)
                    if defender.is_dead():
                        self.team_A.remove(defender)
                        if (defender, "A") in available_characters:
                            available_characters.remove((defender, "A"))

                if len(self.team_A) == 0:
                    print(f"{'=' * 25}\n")
                    print(f"Final turn ({turn_counter}) results\n")
                    self.print_state()
                    print(f"{'=' * 25}\n")
                    print("Winner is team B!")
                    return
                elif len(self.team_B) == 0:
                    print(f"{'=' * 25}\n")
                    print(f"Final turn ({turn_counter}) results\n")
                    self.print_state()
                    print(f"{'=' * 25}\n")
                    print("Winner is team A!")
                    return

            for character in self.team_A + self.team_B:
                character.end_round()

            print(f"{'=' * 25}\n")
