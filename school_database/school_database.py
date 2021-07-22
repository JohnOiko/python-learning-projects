from mod_pupils import *
from teachers import Teachers


def input_menu_choice():
    # read action choice
    action_choice = input("Available actions:\n"
                          "1. Create pupil\n"
                          "2. Print pupil(s)\n"
                          "3. Update pupil\n"
                          "4. Delete pupil\n"
                          "5. Create teacher\n"
                          "6. Print teacher\n"
                          "7. Update teacher\n"
                          "8. Delete teacher\n"
                          "9. Exit application\n\n"
                          "Pick an action: ").strip()
    while action_choice not in [str(number) for number in range(1, 10)]:
        action_choice = input("Pick an action (1 to 9): ")
    print(f"\n{'=' * 75}\n")
    return int(action_choice)


def create_teacher(teachers):
    # read name
    first_name = input("Give first name: ").strip().capitalize()
    while not first_name.isalpha():
        first_name = input("Give first name (must only include letters): ").strip().capitalize()

    # read surname
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
        print()
        teacher.print_teacher()


def update_teacher(teachers):
    # if the teachers database is empty, print an according message and return
    if len(teachers.teachers) == 0:
        print("No teachers saved in the database currently.")
        return

    # else if there are teachers in the database update the teacher that matches the given teacher id
    teachers.update_teacher(teachers.input_teacher_id("update"))


def delete_teacher(teachers):
    teachers.delete_teacher()


def main():
    # load pupils and teachers from the disk
    init_pupils_data()
    teachers = Teachers()

    # print the action menu and read the user's desired action
    print(f"{'=' * 75}\n")
    action_choice = input_menu_choice()

    # keep completing actions until the user chooses to exit the application (action 9)
    while action_choice != 9:
        # perform the action that corresponds to the index of the user's action choice
        if action_choice == 1:
            create_pupil()
        elif action_choice == 2:
            print_existing_pupils()
        elif action_choice == 3:
            update_existing_pupil()
        elif action_choice == 4:
            delete_pupil()
        elif action_choice == 5:
            create_teacher(teachers)
        elif action_choice == 6:
            print_teacher(teachers)
        elif action_choice == 7:
            update_teacher(teachers)
        elif action_choice == 8:
            delete_teacher(teachers)

        # print separator after every completed action and read the next action after printing the main menu
        print(f"\n{'=' * 75}\n")
        action_choice = input_menu_choice()

    # save the pupils' and teachers' data in a json file in the disk
    save_pupils_data()
    teachers.save_teachers_data()

    print(f"Exiting application.\n\n{'=' * 75}")


main()
