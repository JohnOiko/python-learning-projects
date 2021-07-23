class Pupil:
    def __init__(self, first_name="", last_name="", fathers_name="", age=1, pupil_class="1", identity_number="", pupil_id=1001):
        self.first_name = first_name
        self.last_name = last_name
        self.fathers_name = fathers_name
        self.age = age
        self.pupil_class = pupil_class
        self.identity_number = identity_number
        self.pupil_id = pupil_id

    def from_dict(self, pupil):
        self.first_name = pupil["first_name"]
        self.last_name = pupil["last_name"]
        self.fathers_name = pupil["fathers_name"]
        self.age = pupil["age"]
        self.pupil_class = pupil["pupil_class"]
        self.identity_number = pupil["identity_number"] if "identity_number" in pupil.keys() else ""
        self.pupil_id = pupil["pupil_id"]

    def to_dict(self):
        new_pupil_dict = {"first_name": self.first_name, "last_name": self.last_name, "fathers_name": self.fathers_name, "age": self.age, "pupil_class": self.pupil_class}
        if self.identity_number != "":
            new_pupil_dict["identity_number"] = self.identity_number
        new_pupil_dict["pupil_id"] = self.pupil_id
        return new_pupil_dict

    def __str__(self):
        string = f"First name:\t {self.first_name}\n" \
                 f"Last name:\t {self.last_name}\n" \
                 f"Father's name:\t {self.fathers_name}\n" \
                 f"Age:\t {self.age}\n" \
                 f"Class:\t {self.pupil_class}\n"
        if self.identity_number != "":
            string += f"Identity number: {self.identity_number}\n"
        string += f"Pupil id:\t {self.pupil_id}"
        return string.expandtabs(16)
