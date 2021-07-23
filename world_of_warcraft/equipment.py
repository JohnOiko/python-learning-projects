class Equipment:
    def __init__(self, sword, cape):
        self.sword = sword
        self.cape = cape

    def __str__(self):
        return f"S = {round(self.sword, 1)}, C = {round(self.cape, 1)}"

    def __repr__(self):
        return f"Equipment({round(self.sword, 1)}, {round(self.cape, 1)})"
