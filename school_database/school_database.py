from mod_pupils import *
from mod_teachers import *


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


def main():
    # load pupils and teacher from the disk
    init_pupils_data()
    init_teachers_data()

    print(f"{'=' * 75}\n")
    action_choice = input_menu_choice()

    while action_choice != 9:

        # create pupil
        if action_choice == 1:
            create_pupil()

        # print existing pupil(s)
        elif action_choice == 2:
            print_existing_pupils()

        # update existing pupil
        elif action_choice == 3:
            update_existing_pupil()

        # delete existing pupil
        elif action_choice == 4:
            delete_pupil()

        # save new teacher
        elif action_choice == 5:
            save_new_teacher()

        # print existing teacher
        elif action_choice == 6:
            print_existing_teacher()

        # update existing teacher
        elif action_choice == 7:
            update_existing_teacher()

        # delete existing teacher
        elif action_choice == 8:
            delete_teacher(input_teacher_id())

        # print separator after every completed action and read the next action from the main menu
        print(f"\n{'=' * 75}\n")
        action_choice = input_menu_choice()

    # save pupils and teachers data in a json file in the disk
    save_pupils_data()
    save_teachers_data()

    print(f"Exiting application.\n\n{'=' * 75}")


main()
