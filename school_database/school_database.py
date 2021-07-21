# initial pupil database
pupils = [
    {
        "id": 1000,
        "first name": "John",
        "last name": "Doe",
        "fathers name": "Michael",
        "age": 11,
        "class": 1,
        "identity number": "AN123949"
    },
    {
        "id": 1001,
        "first name": "Mary",
        "last name": "Poppins",
        "fathers name": "Chris",
        "age": 10,
        "class": 3,
        "identity number": "AE123981"
    },
    {
        "id": 1002,
        "first name": "John",
        "last name": "Wick",
        "fathers name": "Chiwetel",
        "age": 7,
        "class": 6
    }
]


def input_menu_choice():
    # read action choice
    action_choice = input("Available actions:\n"
                          "1. Save new pupil\n"
                          "2. Print existing pupil\n"
                          "3. Update existing pupil\n"
                          "4. Delete existing pupil\n"
                          "5. Exit application\n\n"
                          "Pick an action: ").strip()
    while action_choice not in {"1", "2", "3", "4", "5"}:
        action_choice = input("Pick an action (1 to 5): ")
    print(f"\n{'=' * 30}\n")
    return int(action_choice)


def print_pupil(pupil):
    max_print_length = 14
    if "identity number" in pupil.keys():
        max_print_length = 16
    print(f"First name:\t {pupil['first name']}\n"
          f"Last name:\t {pupil['last name']}".expandtabs(max_print_length))
    if "identity number" in pupil.keys():
        print(f"Father's name:\t {pupil['fathers name']}".expandtabs(max_print_length))
    else:
        print(f"Father's name: {pupil['fathers name']}")
    print(f"Age:\t {pupil['age']}\n"
          f"Class:\t {pupil['class']}".expandtabs(max_print_length))
    if "identity number" in pupil.keys():
        print(f"Identity number: {pupil['identity number']}")


def next_id():
    new_id = 1000
    for pupil in pupils:
        if pupil["id"] >= new_id:
            new_id = pupil["id"] + 1
    return new_id


def print_pupils_single():
    # read the pupil's id
    id_key = input("Give the id of the student you want printed: ").strip()
    while not id_key.isdigit() or int(id_key) < 1000:
        id_key = input("Give the student's id (must be an integer >= 1000): ").strip()
    print()

    # find the pupil in the database
    for pupil in pupils:
        if pupil["id"] == int(id_key):
            print_pupil(pupil)
            break
    else:
        print("Pupil not in the system.")


def print_pupils_details():
    pupil_counter = 0
    for pupil in pupils:
        pupil_counter += 1
        print_pupil(pupil)
        if pupil_counter < len(pupils):
            print()


def print_pupils_names():
    pupil_counter = 0
    for pupil in pupils:
        pupil_counter += 1
        print(f"Pupil {pupil_counter}: {pupil['first name']} {pupil['fathers name'][0]}. {pupil['last name']}")
        if pupil_counter < len(pupils):
            print()


def create_pupil():
    # minimum and maximum number of classes
    min_class_number = 1
    max_class_number = 6
    pupil_classes = (list(str(number) for number in range(min_class_number, max_class_number + 1)))

    # read first name
    first_name = input("Give first name: ").strip().capitalize()
    while not first_name.isalpha():
        first_name = input("Give first name (must only include letters): ").strip().capitalize()

    # read last name
    last_name = input("Give last name: ").strip().capitalize()
    while not last_name.isalpha():
        last_name = input("Give last name (must only include letters): ").strip().capitalize()

    # read father's name
    fathers_name = input("Give father's name: ").strip().capitalize()
    while not fathers_name.isalpha():
        fathers_name = input("Give father's name (must only include letters): ").strip().capitalize()

    # check if the given name already exist in the pupil database
    create_new_pupil = True
    for pupil in pupils:
        if first_name == pupil["first name"] and last_name == pupil["last name"] \
                and fathers_name == pupil["fathers name"]:
            create_new_pupil = input("\nThere already is a pupil with the same name in the system.\nIf you "
                                     "want to proceed with the new pupil press 1, else press 0: ")
            while create_new_pupil not in ("0", "1"):
                create_new_pupil = input(
                    "If you want to proceed with the new pupil press 1, else press 0 (1 "
                    "or 0): ")
            if int(create_new_pupil) == 1:
                print()
            create_new_pupil = bool(int(create_new_pupil))

    """ if given name didn't already exist in the pupil database of the user chose to keep inputting data, 
        read the rest of the pupil's information """
    if create_new_pupil:

        # read age
        age = input("Give age: ").strip()
        while not age.isdigit() or int(age) <= 0:
            age = input("Give age (must only include one integer): ").strip()

        # read class
        pupil_class = input("Give class: ").strip()
        while pupil_class not in pupil_classes:
            pupil_class = input(f"Give class ({pupil_classes}): ").strip()

        # read identity number
        identity_number = input("Give identity number (0 if no id): ").strip().upper()
        while not identity_number.isalnum() or len(identity_number) < 1:
            identity_number = input(f"Give identity number (must only contain letters and integers): ") \
                .strip().upper()

        # create and save the new pupil
        new_pupil = {
            "id": next_id(),
            "first name": first_name,
            "last name": last_name,
            "fathers name": fathers_name,
            "age": age,
            "class": pupil_class
        }
        if identity_number != '0':
            new_pupil["identity number"] = identity_number

        pupils.append(new_pupil)
        print(f"\n{'=' * 30}\n")
        return new_pupil


def print_pupils():
    # read action choice
    action_choice = input("Available actions:\n"
                          "1. Print single pupil\n"
                          "2. Print all pupils with extensive info\n"
                          "3. Print all pupils with basic info\n\n"
                          "Pick an action: ").strip()
    while action_choice not in {"1", "2", "3"}:
        action_choice = input("Pick an action (1 to 3): ")
    print(f"\n{'=' * 30}\n")
    action_choice = int(action_choice)

    if action_choice == 1:
        print_pupils_single()
    elif action_choice == 2:
        print_pupils_details()
    else:
        print_pupils_names()


def main():
    print(f"{'=' * 30}\n")
    action_choice = input_menu_choice()

    while action_choice != 5:

        # create record action
        if action_choice == 1:
            new_pupil = create_pupil()
            if new_pupil is not None:
                print(f"New pupil saved successfully:\n")
                print_pupil(new_pupil)

        # print existing pupil(s)
        elif action_choice == 2:
            print_pupils()

        # update existing pupil
        elif action_choice == 3:
            print("Action not available yet.")

        # delete existing pupil
        elif action_choice == 4:
            print("Action not available yet.")

        print(f"\n{'=' * 30}\n")
        action_choice = input_menu_choice()

    print(f"Exiting application.\n\n{'=' * 30}")


main()
