from pupils import Pupils
from teachers import Teachers
from lessons import Lessons


def input_menu_choice():
    # read action type choice
    action_type_choice = input("Available actions:\n"
                               "1. Manage pupils\n"
                               "2. Manage teachers\n"
                               "3. Manage lessons\n"
                               "4. Exit application\n\n"
                               "Pick an action: ").strip()
    while action_type_choice not in [str(number) for number in range(1, 5)]:
        action_type_choice = input("Pick an action (1 to 4): ")
    print(f"\n{'=' * 75}\n")
    if action_type_choice == "4":
        return 13

    if action_type_choice == "1":
        action_choice_menu = ("Available actions:\n"
                              "1. Create pupil\n"
                              "2. Print pupil(s)\n"
                              "3. Update pupil\n"
                              "4. Delete pupil\n"
                              "5. Exit application\n\n"
                              "Pick an action: ")
    elif action_type_choice == "2":
        action_choice_menu = ("Available actions:\n"
                              "1. Create teacher\n"
                              "2. Print teacher\n"
                              "3. Update teacher\n"
                              "4. Delete teacher\n"
                              "5. Exit application\n\n"
                              "Pick an action: ")
    else:
        action_choice_menu = ("Available actions:\n"
                              "1. Create lesson\n"
                              "2. Print lesson\n"
                              "3. Update lesson\n"
                              "4. Delete lesson\n"
                              "5. Exit application\n\n"
                              "Pick an action: ")

    action_choice = input(action_choice_menu).strip()
    while action_choice not in [str(number) for number in range(1, 6)]:
        action_choice = input("Pick an action (1 to 5): ")
    print(f"\n{'=' * 75}\n")
    if action_choice == "5":
        return 13
    return (int(action_type_choice) - 1) * 4 + int(action_choice)


def create_pupil(pupils):
    pupils.create_pupil()


def print_pupils(pupils):
    # if the pupils database is empty, print an according message and return
    if len(pupils.pupils) == 0:
        print("No pupils saved in the database currently.")
        return

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
        # read the pupil's id
        pupil_id = input("Give the id of the student you want printed: ").strip()
        while not pupil_id.isdigit() or int(pupil_id) <= 1000:
            pupil_id = input("Give the student's id (must be an integer >= 1000): ").strip()
        print()

        # find the pupil in the database
        pupil = pupils.search_pupil_by_id(pupil_id)
        if pupil is not None:
            print(f"{pupil}")
        else:
            print("Pupil not in the system.")
    elif action_choice == 2:
        print(pupils)
    else:
        pupils.print_pupils_names()


def update_pupil(pupils):
    # read search type
    search_type = input("Do you want to search by id (\"i\") or by last name (\"s\"): ").strip().lower()
    while search_type != "i" and search_type != "s":
        search_type = input("Pick a valid search method (\"i\" for id or \"s\" for last name): ").strip().lower()

    # search by id
    if search_type == "i":
        # read id to search for
        pupil_id = input("Give an id to search for: ").strip()
        if not pupil_id.isdigit() or int(pupil_id) <= 1000:
            pupil_id = input("Give an id to search for (must be an integer >= 1000): ").strip()
        pupil_id = int(pupil_id)

        pupils.pupil_update(pupil_id)

    # search by last name
    else:
        # read last name to search for
        last_name = input("Give a last name to search for: ").strip().capitalize()
        if not last_name.isalpha() or len(last_name) < 1:
            last_name = input("Give a valid last name to search for: ").strip().capitalize()

        pupils_to_be_updated = pupils.search_pupil_by_last_name(last_name)
        # if no pupils with the searched for last name were found print error message
        if len(pupils_to_be_updated) == 0:
            print("There is no pupils in the database with the given last name.")

        # else if only one pupil was found update their information
        elif len(pupils_to_be_updated) == 1:
            print(f"\n{'=' * 75}\n")
            print(f"{pupils_to_be_updated[0]}\n\n{'=' * 75}\n")
            pupils.input_updated_details(pupils_to_be_updated[0])

        # else if more than one pupils were found, let the user pick one based on their id and update their information
        else:
            # print each pupil found and their id
            print("Here is the list of students that match the last name you entered:")
            for pupil in pupils_to_be_updated:
                print(f"\n{pupil}")

            # keep reading ids until the one given exists in the list of pupils found with the given last name
            pupil_to_be_updated = None
            pupil_id = input("\nGive the id of the pupil whose details you want to update: ").strip()
            if pupil_id.isdigit() and int(pupil_id) > 1000:
                for pupil in pupils_to_be_updated:
                    if pupil.pupil_id == int(pupil_id):
                        pupil_to_be_updated = pupil
                        break
            while pupil_to_be_updated is None:
                pupil_id = input("Give the id of the pupil whose details you want to update: ")
                if pupil_id.isdigit() and int(pupil_id) > 1000:
                    for pupil in pupils_to_be_updated:
                        if pupil.pupil_id == int(pupil_id):
                            pupil_to_be_updated = pupil
                            break
            print(f"\n{'=' * 75}\n")

            # update the information of the pupil chosen based on their last name and id
            pupils.input_updated_details(pupil_to_be_updated)


def delete_pupil(pupils, lessons):
    # read search type for deletion
    deletion_type = input("Do you want to delete by id (\"i\") or by last name (\"s\"): ").strip().lower()
    while deletion_type != "i" and deletion_type != "s":
        deletion_type = input("Pick a valid deletion method (\"i\" for id or \"s\" for last name): ").strip().lower()

    # delete by id
    if deletion_type == "i":
        # read id to search for
        pupil_id = input("Give the id of the student you want to delete: ").strip()
        if not pupil_id.isdigit() or int(pupil_id) <= 1000:
            pupil_id = input("Give the id of the student you want to delete (must be an integer > 1000): ").strip()
        pupil_id = int(pupil_id)

        pupils.delete_pupil_by_id(pupil_id)
        lessons.delete_pupil(pupil_id)

    # search by last name
    else:
        # read last name to search for
        last_name = input("Give the last name of the student you want to delete: ").strip().capitalize()
        if not last_name.isalpha() or len(last_name) < 1:
            last_name = input("Give the valid last name of the student you want to delete: ") \
                .strip().capitalize()

        pupils_to_be_deleted = pupils.search_pupil_by_last_name(last_name)

        # if no pupils with the searched for last name were found print error message
        if len(pupils_to_be_deleted) == 0:
            print("There are no pupils in the database with the given last name.")

        # else if only one pupil was found delete them
        elif len(pupils_to_be_deleted) == 1:
            pupils.delete_pupil_by_id(pupils_to_be_deleted[0].pupil_id)
            lessons.delete_pupil(pupils_to_be_deleted[0].pupil_id)

        # else if more than one pupils were found, let the user pick one based on their id and delete them
        else:
            # print each pupil found and their id
            print("Here is the list of students that match the last name you entered:")
            for pupil in pupils_to_be_deleted:
                print(f"\n{pupil}")

            # keep reading ids until the one given exists in the list of pupils found with the given last name
            pupil_to_be_deleted = None
            pupil_id = input("\nGive the id of the pupil you want to delete: ").strip()
            if pupil_id.isdigit() and int(pupil_id) > 1000:
                for pupil in pupils_to_be_deleted:
                    if pupil.pupil_id == int(pupil_id):
                        pupil_to_be_deleted = pupil
                        break
            while pupil_to_be_deleted is None:
                pupil_id = input("Give the id of the pupil you want to delete: ")
                if pupil_id.isdigit() and int(pupil_id) > 1000:
                    for pupil in pupils_to_be_deleted:
                        if pupil.pupil_id == int(pupil_id):
                            pupil_to_be_deleted = pupil
                            break
            print(f"\n{'=' * 75}\n")

            # delete the selected pupil
            pupils.delete_pupil_by_id(pupils_to_be_deleted[0].pupil_id)
            lessons.delete_pupil(pupils_to_be_deleted[0].pupil_id)


def create_teacher(teachers):
    # read name
    first_name = input("Give first name: ").strip().capitalize()
    while not first_name.isalpha():
        first_name = input("Give first name (must only include letters): ").strip().capitalize()

    # read last name
    last_name = input("Give last name:\t ".expandtabs(16)).strip().capitalize()
    while not last_name.isalpha():
        last_name = input("Give last name (must only include letters): ").strip().capitalize()

    # create the new teacher
    teachers.create_teacher(first_name, last_name)


def print_teacher(teachers):
    # if the teachers database is empty, print an according message and return
    if len(teachers.teachers) == 0:
        print("No teachers saved in the database currently.")
        return

    # else find the teacher that matches the given teacher id and print their information
    teacher = teachers.read_teacher(teachers.input_teacher_id("print"))
    if teacher is None:
        print("No teacher with the given id in the database.")
    else:
        print(f"\n{teacher}")


def update_teacher(teachers):
    # if the teachers database is empty, print an according message and return
    if len(teachers.teachers) == 0:
        print("No teachers saved in the database currently.")
        return

    # else if there are teachers in the database update the teacher that matches the given teacher id
    teachers.update_teacher(teachers.input_teacher_id("update"))


def delete_teacher(teachers, lessons):
    teachers.delete_teacher(lessons)


def create_lesson(lessons):
    # read lesson name
    lesson_name = input("Give lesson's name: ").strip().capitalize()
    while not lesson_name.isalpha():
        lesson_name = input("Give lesson's name (must only include letters): ").strip().capitalize()

    # create the new teacher
    lessons.create_lesson(lesson_name)


def print_lesson(lessons, teachers, pupils):
    # if the lessons database is empty, print an according message and return
    if len(lessons.lessons) == 0:
        print("No lessons saved in the database currently.")
        return

    # else find the lesson that matches the given lesson id and print their information
    lesson = lessons.read_lesson(lessons.input_lesson_id("print"))
    if lesson is None:
        print("No lesson with the given id in the database.")
    else:
        print(f"\n{lesson.to_string(teachers, pupils)}")


def update_lesson(lessons, teachers, pupils):
    # if the lessons database is empty, print an according message and return
    if len(lessons.lessons) == 0:
        print("No lessons saved in the database currently.")
        return

    # else if there are lessons in the database update the lesson that matches the given lesson id
    lessons.update_lesson(lessons.input_lesson_id("update"), teachers, pupils)


def delete_lesson(lessons):
    lessons.delete_lesson()


def main():
    # load pupils and teachers from the disk
    pupils = Pupils()
    teachers = Teachers()
    lessons = Lessons()

    # print the action menu and read the user's desired action
    print(f"{'=' * 75}\n")
    action_choice = input_menu_choice()

    # keep completing actions until the user chooses to exit the application (action 9)
    while action_choice != 13:
        # perform the action that corresponds to the index of the user's action choice
        if action_choice == 1:
            create_pupil(pupils)
        elif action_choice == 2:
            print_pupils(pupils)
        elif action_choice == 3:
            update_pupil(pupils)
        elif action_choice == 4:
            delete_pupil(pupils, lessons)
        elif action_choice == 5:
            create_teacher(teachers)
        elif action_choice == 6:
            print_teacher(teachers)
        elif action_choice == 7:
            update_teacher(teachers)
        elif action_choice == 8:
            delete_teacher(teachers, lessons)
        elif action_choice == 9:
            create_lesson(lessons)
        elif action_choice == 10:
            print_lesson(lessons, teachers, pupils)
        elif action_choice == 11:
            update_lesson(lessons, teachers, pupils)
        elif action_choice == 12:
            delete_lesson(lessons)

        # print separator after every completed action and read the next action after printing the main menu
        print(f"\n{'=' * 75}\n")
        action_choice = input_menu_choice()

    # save the pupils' and teachers' data in a json file in the disk
    pupils.save_pupils_data()
    teachers.save_teachers_data()
    lessons.save_lessons_data()

    print(f"Exiting application.\n\n{'=' * 75}")


main()
