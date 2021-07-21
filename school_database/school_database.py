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
    print(f"\n{'=' * 75}\n")
    return int(action_choice)


def print_pupil(pupil):
    print(f"First name:\t {pupil['first name']}".expandtabs(16))
    print(f"Last name:\t {pupil['last name']}".expandtabs(16))
    print(f"Father's name:\t {pupil['fathers name']}".expandtabs(16))
    print(f"Age:\t {pupil['age']}".expandtabs(16))
    print(f"Class:\t {pupil['class']}".expandtabs(16))
    if "identity number" in pupil.keys():
        print(f"Identity number: {pupil['identity number']}")


def next_id():
    new_id = 1000
    for pupil in pupils:
        if pupil["id"] >= new_id:
            new_id = pupil["id"] + 1
    return new_id


def input_updated_details(pupil):
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
        updated_first_name = input("Give updated first name: ").strip().capitalize()
        while not updated_first_name.isalpha() or len(updated_first_name) < 1:
            updated_first_name = input("Give valid updated first name: ").strip().capitalize()
        pupil["first name"] = updated_first_name
    elif action_choice == 2:
        updated_last_name = input("Give updated last name: ").strip().capitalize()
        while not updated_last_name.isalpha() or len(updated_last_name) < 1:
            updated_last_name = input("Give valid updated last name: ").strip().capitalize()
        pupil["last name"] = updated_last_name
    elif action_choice == 3:
        updated_fathers_name = input("Give updated father's name: ").strip().capitalize()
        while not updated_fathers_name.isalpha() or len(updated_fathers_name) < 1:
            updated_fathers_name = input("Give valid updated father's name: ").strip().capitalize()
        pupil["fathers name"] = updated_fathers_name
    elif action_choice == 4:
        updated_age = input("Give updated age: ").strip()
        while not updated_age.isdigit() or int(updated_age) < 0:
            updated_age = input("Give valid updated age: ").strip()
        pupil["age"] = int(updated_age)
    elif action_choice == 5:
        updated_class = input("Give updated class: ").strip()
        while not updated_class.isdigit() or int(updated_class) < 0:
            updated_class = input("Give valid class: ").strip()
        pupil["class"] = int(updated_class)
    else:
        updated_identity_number = input("Give updated identity number: ").strip().upper()
        while not (updated_identity_number.isalnum() and len(updated_identity_number) > 0
                   or updated_identity_number == ""):
            updated_identity_number = input("Give valid updated identity number "
                                            "(or leave empty for no identity number): ").strip().upper()
        if updated_identity_number == "":
            pupil.pop("identity number")
        else:
            pupil["identity number"] = updated_identity_number
    print("Pupil's details successfully updated.")


def print_pupils_single():
    # read the pupil's id
    id_key = input("Give the id of the student you want printed: ").strip()
    while not id_key.isdigit() or int(id_key) < 1000:
        id_key = input("Give the student's id (must be an integer >= 1000): ").strip()
    print()

    # find the pupil in the database
    pupil = search_pupil_by_id(id_key)
    if pupil is not None:
        print_pupil(pupil)
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


def search_pupil_by_name(surname):
    return [pupil for pupil in pupils if pupil["last name"] == surname]


def search_pupil_by_id(id_key):
    for pupil in pupils:
        if pupil["id"] == int(id_key):
            return pupil


def create_pupil():
    # minimum and maximum number of classes
    min_class_number = 1
    max_class_number = 6
    pupil_classes = (list(str(number) for number in range(min_class_number, max_class_number + 1)))

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
        new_pupil = {
            "id": next_id(),
            "first name": first_name,
            "last name": last_name,
            "fathers name": fathers_name,
            "age": age,
            "class": pupil_class
        }
        if identity_number != "":
            new_pupil["identity number"] = identity_number

        pupils.append(new_pupil)
        print(f"\n{'=' * 75}\n")
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
    print(f"\n{'=' * 75}\n")
    action_choice = int(action_choice)

    if action_choice == 1:
        print_pupils_single()
    elif action_choice == 2:
        print_pupils_details()
    else:
        print_pupils_names()


def update_pupil():
    # read search type
    search_type = input("Do you want to search by id (\"i\") or by surname (\"s\"): ").strip().lower()
    while search_type != "i" and search_type != "s":
        search_type = input("Pick a valid search method (\"i\" for id or \"s\" for surname): ").strip().lower()

    # search by id
    if search_type == "i":
        # read id to search for
        id_key = input("Give an id to search for: ").strip()
        if not id_key.isdigit() or int(id_key) < 1000:
            id_key = input("Give an id to search for (must be an integer >= 1000): ").strip()
        id_key = int(id_key)
        print(f"\n{'=' * 75}\n")

        # if a student with the given id doesn't exist print an error message, else update their details
        pupil_to_be_updated = search_pupil_by_id(id_key)
        if pupil_to_be_updated is None:
            print("There is no pupil in the database with the given id")
        else:
            print_pupil(pupil_to_be_updated)
            print(f"\n{'=' * 75}\n")
            input_updated_details(pupil_to_be_updated)
    # search by surname
    else:
        # read surname to search for
        surname_key = input("Give a surname to search for: ").strip().capitalize()
        if not surname_key.isalpha() or len(surname_key) < 1:
            surname_key = input("Give a valid surname to search for: ").strip().capitalize()
        print(f"\n{'=' * 75}\n")

        pupils_to_be_updated = search_pupil_by_name(surname_key)
        # if no pupils with the searched for surname were found print error message
        if len(pupils_to_be_updated) == 0:
            print("There is no pupils in the database with the given surname.")
        # else if only one pupil was found update their information
        elif len(pupils_to_be_updated) == 1:
            print_pupil(pupils_to_be_updated[0])
            print(f"\n{'=' * 75}\n")
            input_updated_details(pupils_to_be_updated[0])
        # else if more than one pupils were found, let the user pick one based on their id and update their information
        else:
            # print each pupil found and their id
            print("Here is the list of students that have the surname you entered:\n")
            for pupil in pupils_to_be_updated:
                print(f"Id: {pupil['id']}")
                print_pupil(pupil)
                print()

            # keep reading ids until the one given exists in the list of pupils found with the given surname
            pupil_to_be_updated = None
            id_key = input("Give the id of the pupil whose details you want to update: ").strip()
            if id_key.isdigit() and int(id_key) >= 1000:
                for pupil in pupils_to_be_updated:
                    if pupil["id"] == int(id_key):
                        pupil_to_be_updated = pupil
                        break
                while pupil_to_be_updated is None:
                    id_key = input("Give the id of the pupil whose details you want to update: ")
                    if id_key.isdigit() and int(id_key) >= 1000:
                        for pupil in pupils_to_be_updated:
                            if pupil["id"] == int(id_key):
                                pupil_to_be_updated = pupil
                                break
            print(f"\n{'=' * 75}\n")

            # update the information of the pupil chosen based on their surname and id
            input_updated_details(pupil_to_be_updated)


def main():
    print(f"{'=' * 75}\n")
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
            update_pupil()

        # delete existing pupil
        elif action_choice == 4:
            print("Action not available yet.")

        print(f"\n{'=' * 75}\n")
        action_choice = input_menu_choice()

    print(f"Exiting application.\n\n{'=' * 75}")


main()
