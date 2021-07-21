# current student database
students = [
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

# minimum and maximum number of class
min_class_number = 1
max_class_number = 6

menu_string = ("Available actions:\n"
               "1. Save new student\n"
               "2. Print existing student\n"
               "3. Update existing student\n"
               "4. Delete existing student\n"
               "5. Exit application\n\n"
               "Pick an action: ")

separator_string = f"\n{'=' * 30}\n"

student_classes = (list(str(number) for number in range(min_class_number, max_class_number + 1)))

# this is when the user starts interacting with the application
print(f"{'=' * 30}\n")

# read action choice
action_choice = input(menu_string).strip()
while action_choice not in {"1", "2", "3", "4", "5", "5"}:
    action_choice = input("Pick an action (1 to 5): ")
action_choice = int(action_choice)
print(separator_string)

while action_choice != 5: \
 \
        # create record action
        if action_choice == 1:

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

            # check if the given name already exist in the student database
            create_new_student = True
            for student in students:
                if first_name == student["first name"] and last_name == student["last name"] \
                        and fathers_name == student["fathers name"]:
                    create_new_student = input("\nThere already is a student with the same name in the system.\nIf you "
                                               "want to proceed with the new student press 1, else press 0: ")
                    while create_new_student not in ("0", "1"):
                        create_new_student = input("If you want to proceed with the new student press 1, else press 0 (1 "
                                                   "or 0): ")
                    if int(create_new_student) == 1:
                        print()
                    create_new_student = bool(int(create_new_student))

            """if given name didn't already exist in the student database of the user chose to keep inputting data, 
            read the rest of the student's information """
            if create_new_student:

                # read age
                age = input("Give age: ").strip()
                while not age.isdigit() or int(age) <= 0:
                    age = input("Give age (must only include one integer): ").strip()

                # read class
                student_class = input("Give class: ").strip()
                while student_class not in student_classes:
                    student_class = input(f"Give class ({student_classes}): ").strip()

                # read identity number
                identity_number = input("Give identity number (0 if no id): ").strip().upper()
                while not identity_number.isalnum() or len(identity_number) < 1:
                    identity_number = input(f"Give identity number (must only contain letters and integers): ") \
                        .strip().upper()

                # calculate the new student's id
                new_id = 1000
                for student in students:
                    if student["id"] >= new_id:
                        new_id = student["id"]

                # add the new student to the student database
                new_student = {
                    "id": new_id,
                    "first name": first_name,
                    "last name": last_name,
                    "fathers name": fathers_name,
                    "age": age,
                    "class": student_class
                }

                if identity_number != '0':
                    new_student["identity number"] = identity_number
                students.append(new_student)

                print(separator_string)

                # print the information of the new student
                max_print_length = 14
                if "identity number" in new_student.keys():
                    max_print_length = 16
                print(f"New student saved successfully:\n")
                print(f"First name:\t {new_student['first name']}\n"
                      f"Last name:\t {new_student['last name']}".expandtabs(max_print_length))
                if "identity number" in new_student.keys():
                    print(f"Father's name:\t {new_student['fathers name']}".expandtabs(max_print_length))
                else:
                    print(f"Father's name: {new_student['fathers name']}")
                print(f"Age:\t {new_student['age']}\n"
                      f"Class:\t {new_student['class']}".expandtabs(max_print_length))
                if "identity number" in new_student.keys():
                    print(f"Identity number: {new_student['identity number']}")

        # if the chosen action has not been implemented yet, print an according message
        elif action_choice in [2, 3, 4, 5]:
            print("Action not available yet.")

        print(separator_string)

        # read action choice
        action_choice = input(menu_string).strip()
        while action_choice not in {"1", "2", "3", "4", "5", "5"}:
            action_choice = input("Pick an action (1 to 5): ")
        action_choice = int(action_choice)
        print(separator_string)

# once the user has chosen the fifth action the loop is broken and an exit message is printed
print(f"Exiting application.\n\n{'=' * 30}")
