from pupil import Pupil
import json


class Pupils:
    def __init__(self):
        try:
            with open("pupils.json", "r") as f:
                self.pupils = []
                for pupil_dict in json.load(f):
                    pupil = Pupil()
                    pupil.from_dict(pupil_dict)
                    self.pupils.append(pupil)
        except FileNotFoundError:
            self.pupils = []

    def save_pupils_data(self):
        with open("pupils.json", "w") as f:
            json.dump([pupil.to_dict() for pupil in self.pupils], f)

    def next_id(self):
        next_id = 1001
        for pupil in self.pupils:
            if pupil.pupil_id >= next_id:
                next_id = pupil.pupil_id + 1
        return next_id

    def input_updated_details(self, pupil):
        # print the students current information
        print(f"{pupil}\n\n{'=' * 75}\n")

        # print the menu of actions and read the user's choice
        action_choice = input("Available actions:\n"
                              "1. Update first name\n"
                              "2. Update last name\n"
                              "3. Update father's name\n"
                              "4. Update age\n"
                              "5. Update class\n"
                              "6. Update identity number\n\n"
                              "Pick an action: ").strip()
        while action_choice not in {"1", "2", "3", "4", "5", "6"}:
            action_choice = input("Pick an action (1 to 6): ")
        print(f"\n{'=' * 75}\n")
        action_choice = int(action_choice)

        # update the information the user chose to update
        if action_choice == 1:
            first_name = input("Give updated first name: ").strip().capitalize()
            while not first_name.isalpha() or len(first_name) < 1:
                first_name = input("Give valid updated first name: ").strip().capitalize()
            pupil.first_name = first_name
        elif action_choice == 2:
            last_name = input("Give updated last name: ").strip().capitalize()
            while not last_name.isalpha() or len(last_name) < 1:
                last_name = input("Give valid updated last name: ").strip().capitalize()
            pupil.last_name = last_name
        elif action_choice == 3:
            fathers_name = input("Give updated father's name: ").strip().capitalize()
            while not fathers_name.isalpha() or len(fathers_name) < 1:
                fathers_name = input("Give valid updated father's name: ").strip().capitalize()
            pupil.fathers_name = fathers_name
        elif action_choice == 4:
            age = input("Give updated age: ").strip()
            while not age.isdigit() or int(age) < 0:
                age = input("Give valid updated age: ").strip()
            pupil.age = int(age)
        elif action_choice == 5:
            pupil_class = input("Give updated class: ").strip()
            while not pupil_class.isdigit() or int(pupil_class) < 0:
                pupil_class = input("Give valid class: ").strip()
            pupil.pupil_class = int(pupil_class)
        else:
            identity_number = input("Give updated identity number: ").strip().upper()
            while not (identity_number.isalnum() and len(identity_number) > 0
                       or identity_number == ""):
                identity_number = input("Give valid updated identity number (or leave empty for no identity "
                                        "number): ").strip().upper()
            pupil.identity_number = identity_number
        print("Pupil's details successfully updated.")

    def create_pupil(self):
        # available classes
        pupil_classes = ["1", "2", "3", "4", "5", "6"]

        # read first name
        first_name = input("Give first name:\t ".expandtabs(21)).strip().capitalize()
        while not first_name.isalpha():
            first_name = input("Give first name (must only include letters): ").strip().capitalize()

        # read last name
        last_name = input("Give last name:\t ".expandtabs(21)).strip().capitalize()
        while not last_name.isalpha():
            last_name = input("Give last name (must only include letters): ").strip().capitalize()

        # read father's name
        fathers_name = input("Give father's name:\t ".expandtabs(21)).strip().capitalize()
        while not fathers_name.isalpha():
            fathers_name = input("Give father's name (must only include letters): ").strip().capitalize()

        # if there is at least one pupil in the database check if the given name already exists in the pupil database
        create_new_pupil = True
        if len(self.pupils) > 0:
            for pupil in self.pupils:
                if first_name == pupil.first_name and last_name == pupil.last_name \
                        and fathers_name == pupil.fathers_name:
                    create_new_pupil = input("\nThere already is a pupil with the same name in the system.\nIf you "
                                             "want to proceed with the new pupil press 1, else press 0: ")
                    while create_new_pupil not in ("0", "1"):
                        create_new_pupil = input(
                            "If you want to proceed with the new pupil press 1, else press 0 (1 "
                            "or 0): ")
                    if int(create_new_pupil) == 1:
                        print(f"\n{'=' * 75}\n")
                    else:
                        return
                    create_new_pupil = bool(int(create_new_pupil))

        """ if given name didn't already exist in the pupil database of the user chose to keep inputting data, 
            read the rest of the pupil's information """
        if create_new_pupil:

            # read age
            age = input("Give age:\t ".expandtabs(21)).strip()
            while not age.isdigit() or int(age) <= 0:
                age = input("Give age (must only include one integer): ").strip()

            # read class
            pupil_class = input("Give class:\t ".expandtabs(21)).strip()
            while pupil_class not in pupil_classes:
                pupil_class = input(f"Give class ({pupil_classes}): ").strip()

            # read identity number
            identity_number = input("Give identity number: ").strip().upper()
            while not (identity_number.isalnum() and len(identity_number) > 0 or identity_number == ""):
                identity_number = input(f"Give valid identity number (leave empty for no identity number): ") \
                    .strip().upper()

            # create and save the new pupil
            new_pupil = Pupil(first_name, last_name, fathers_name, age, pupil_class, identity_number, self.next_id())
            self.pupils.append(new_pupil)
            print(f"\n{'=' * 75}\n")
            print(f"New pupil saved successfully:\n\n{new_pupil}")

    def search_pupil_by_id(self, pupil_id):
        for pupil in self.pupils:
            if pupil.pupil_id == int(pupil_id):
                return pupil

    def search_pupil_by_last_name(self, last_name):
        return [pupil for pupil in self.pupils if pupil.last_name == last_name]

    def pupil_update(self, pupil_id):
        # if a student with the given id doesn't exist print an error message, else update their details
        pupil = self.search_pupil_by_id(pupil_id)
        if pupil is None:
            print("There is no pupil in the database with the given id.")
            return

        print(f"\n{'=' * 75}\n")
        self.input_updated_details(pupil)

    def delete_pupil_by_id(self, pupil_id):
        pupil = self.search_pupil_by_id(pupil_id)
        if pupil is not None:
            self.pupils.remove(pupil)
            print("Pupil successfully deleted.")
        else:
            print("There are no pupils in the database with the given id.")

    def print_pupils_names(self):
        for pupil in self.pupils:
            print(f"{pupil.pupil_id}: {pupil.first_name} {pupil.fathers_name}. {pupil.last_name}")

    def __str__(self):
        return "\n\n".join([str(pupil) for pupil in self.pupils])
