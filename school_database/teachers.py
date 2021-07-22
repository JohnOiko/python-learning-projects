from teacher import Teacher
import json


class Teachers:
    def __init__(self):
        try:
            with open("teachers.json", "r") as f:
                self.teachers = []
                for teacher_dict in json.load(f):
                    teacher = Teacher()
                    teacher.from_dict(teacher_dict)
                    self.teachers.append(teacher)
        except FileNotFoundError:
            self.teachers = []

    def save_teachers_data(self):
        with open("teachers.json", "w") as f:
            json.dump([teacher.to_dict() for teacher in self.teachers], f)

    def next_id(self):
        next_id = 1
        for teacher in self.teachers:
            if teacher.teacher_id >= next_id:
                next_id = teacher.teacher_id + 1
        return next_id

    def input_teacher_id(self, action_type):
        teacher_id = input(f"Give the id of the teacher whose information you want to {action_type}: ").strip()
        if not teacher_id.isdigit() or int(teacher_id) < 1:
            teacher_id = input("Give the id of the teacher whose information you want to {action_type} "
                               "(must be a positive integer): ").strip()
        return int(teacher_id)

    def create_teacher(self, first_name, last_name):
        new_teacher = Teacher(first_name, last_name, self.next_id())

        # if the teacher isn't already in the database add them to the database and update the corresponding flag
        teacher_created = False
        for teacher in self.teachers:
            if teacher.first_name == first_name and teacher.last_name == last_name:
                break
        else:
            self.teachers.append(new_teacher)
            teacher_created = True

        # print the according messages
        if teacher_created:
            print(f"\n{'=' * 75}\n")
            print("New teacher successfully saved:\n")
            new_teacher.print_teacher()
        else:
            print("\nTeacher already in the database.")

    def read_teacher(self, teacher_id):
        for teacher in self.teachers:
            if teacher.teacher_id == int(teacher_id):
                return teacher

    def update_teacher(self, teacher_id):
        teacher = self.read_teacher(teacher_id)
        if teacher is not None:

            update_choice = input("Do you want to change the teacher's first or last name (1 for first, 2 for last): ") \
                .strip()
            while update_choice != "1" and update_choice != "2":
                update_choice = input("Do you want to change the teacher's first or last name "
                                      "(1 for first, 2 for last): ").strip()

            if update_choice == "1":
                updated_first_name = input("\nGive updated first name: ").strip().capitalize()
                while not updated_first_name.isalpha():
                    updated_first_name = input("Give a valid updated first name: ").strip().capitalize()
                teacher.first_name = updated_first_name
            else:
                updated_last_name = input("\nGive updated last name: ").strip().capitalize()
                while not updated_last_name.isalpha():
                    updated_last_name = input("Give a valid updated last name: ").strip().capitalize()
                teacher.last_name = updated_last_name

            print(f"Teacher's {'first' if update_choice == '1' else 'last'} name updated successfully.")
        else:
            print("\nNo teacher with the given id found in the database.")

    def delete_teacher(self):
        teacher = self.read_teacher(self.input_teacher_id("delete"))

        if teacher is None:
            print("No teacher with the given id found in the database.")
        else:
            self.teachers.remove(teacher)
            print("Teacher deleted successfully.")
