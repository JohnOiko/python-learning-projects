import json

# initial teacher database
teachers = []


def init_teachers_data():
    global teachers
    try:
        with open("teachers.json", "r") as f:
            teachers = json.load(f)
    except FileNotFoundError:
        teachers = []


def save_teachers_data():
    with open("teachers.json", "w") as f:
        json.dump(teachers, f)


def input_teacher_id():
    # read id
    id_key = input("Give teacher's id: ").strip()
    if not id_key.isdigit() or int(id_key) < 1000:
        id_key = input("Give teacher's id (must be an integer >= 1000): ").strip()
    id_key = int(id_key)
    return id_key


def next_id():
    new_id = 1000
    for teacher in teachers:
        if teacher["teacher_id"] >= new_id:
            new_id = teacher["teacher_id"] + 1
    return new_id


def read_teacher(id_key):
    for teacher in teachers:
        if teacher["teacher_id"] == int(id_key):
            return teacher


def update_teacher(id_key, key, updated_value):
    teacher_to_be_updated = read_teacher(id_key)
    if teacher_to_be_updated is not None:
        teacher_to_be_updated[key] = updated_value
        print(f"Teacher's {key} updated successfully.")


def create_teacher(name, surname):
    new_teacher = {"teacher_id": next_id(), "name": name, "surname": surname}
    # if the teacher isn't already in the database add them to the database and update the corresponding flag
    teacher_created = False
    for teacher in teachers:
        if teacher["name"] == name and teacher["surname"] == surname:
            break
    else:
        teachers.append(new_teacher)
        teacher_created = True

    # print the according messages
    if teacher_created:
        print(f"\n{'=' * 75}\n")
        print("New teacher successfully saved:\n")
        print(f"Name:\t {new_teacher['name']}".expandtabs(8))
        print(f"Surname: {new_teacher['surname']}".expandtabs(8))
    else:
        print("\nTeacher already in the database.")


def save_new_teacher():
    # read name
    name = input("Give name:\t ".expandtabs(13)).strip().capitalize()
    while not name.isalpha():
        name = input("Give name (must only include letters): ").strip().capitalize()

    # read surname
    surname = input("Give surname: ").strip().capitalize()
    while not surname.isalpha():
        surname = input("Give surname (must only include letters): ").strip().capitalize()

    create_teacher(name, surname)


def print_existing_teacher():

    # if the teachers database is empty, print an according message and return
    if len(teachers) == 0:
        print("No teachers saved in the database currently.")
        return

    teacher_to_be_printed = read_teacher(input_teacher_id())
    if teacher_to_be_printed is None:
        print("No teacher with the given id in the database.")
    else:
        print()
        print(f"Name:\t {teacher_to_be_printed['name']}".expandtabs(8))
        print(f"Surname: {teacher_to_be_printed['surname']}".expandtabs(8))


def update_existing_teacher():
    id_key = input_teacher_id()
    if read_teacher(id_key) is not None:
        updated_name = input("\nGive updated name (leave empty for no change): ")
        while not updated_name.isalpha() and not updated_name == "":
            updated_name = input("Give updated name (leave empty for no change): ")
        if updated_name != "":
            update_teacher(id_key, "name", updated_name)

        updated_surname = input("\nGive updated surname (leave empty for no change): ")
        while not updated_surname.isalpha() and not updated_surname == "":
            updated_surname = input("Give updated surname (leave empty for no change): ")
        if updated_surname != "":
            update_teacher(id_key, "surname", updated_surname)
    else:
        print("\nNo teacher with the given id found in the database.")


def delete_teacher(id_key):
    teacher_to_be_deleted = read_teacher(id_key)
    if teacher_to_be_deleted is None:
        print("No teacher with the given id found in the database.")
    else:
        teachers.remove(teacher_to_be_deleted)
        print("Teacher deleted successfully.")
