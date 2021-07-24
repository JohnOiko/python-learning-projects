from lesson import Lesson
from pupils import Pupils
from teachers import Teachers
import json

class Lessons:
    def __init__(self):
        try:
            with open("lessons.json", "r") as f:
                self.lessons = []
                for lesson_dict in json.load(f):
                    lesson = Lesson()
                    lesson.from_dict(lesson_dict)
                    self.lessons.append(lesson)
        except FileNotFoundError:
            self.lessons = []

    def save_lessons_data(self):
        with open("lessons.json", "w") as f:
            json.dump([lesson.to_dict() for lesson in self.lessons], f)

    def next_id(self):
        next_id = 10001
        for lesson in self.lessons:
            if lesson.lesson_id >= next_id:
                next_id = lesson.lesson_id + 1
        return next_id

    def input_lesson_id(self, action_type):
        lesson_id = input(f"Give the id of the lesson whose information you want to {action_type}: ").strip()
        if not lesson_id.isdigit() or int(lesson_id) < 1:
            teacher_id = input(f"Give the id of the lesson whose information you want to {action_type} "
                               "(must be an integer > 10000): ").strip()
        return int(lesson_id)

    def create_lesson(self, lesson_name):
        new_lesson = Lesson(lesson_name, self.next_id())

        # if the lesson isn't already in the database add it to the database and update the corresponding flag
        lesson_created = False
        for lesson in self.lessons:
            if lesson.lesson_name == lesson_name:
                break
        else:
            self.lessons.append(new_lesson)
            lesson_created = True

        # print the according messages
        if lesson_created:
            print(f"\n{'=' * 75}\n")
            print("New lesson successfully saved:\n")
            print(f"Lesson name: {new_lesson.lesson_name}\nLesson id:\t {new_lesson.lesson_id}".expandtabs(12))
        else:
            print("Lesson already in the database.")

    def read_lesson(self, lesson_id):
        for lesson in self.lessons:
            if lesson.lesson_id == int(lesson_id):
                return lesson

    def update_lesson(self, lesson_id, teachers, pupils):
        lesson = self.read_lesson(lesson_id)
        if lesson is not None:

            update_choice = input("Do you want to change the lesson's name, update teachers or update pupils "
                                  "(1 for name, 2 for teachers, 3 for pupils): ").strip()
            while update_choice not in ["1", "2", "3"]:
                update_choice = input("Do you want to change the lesson's name, update teachers or update pupils "
                                      "(1 for name, 2 for teachers, 3 for pupils): ").strip()

            if update_choice == "1":
                lesson_name = input("\nGive updated name: ").strip().capitalize()
                while not lesson_name.isascii():
                    lesson_name = input("Give a valid updated name: ").strip().capitalize()
                lesson.lesson_name = lesson_name

            elif update_choice == "2":
                add_or_remove = input("Do you want to add or remove a teacher (1 add, 2 remove): ").strip()
                while update_choice not in ["1", "2"]:
                    add_or_remove = input("Do you want to add or remove a teacher (1 add, 2 remove): ").strip()

                teacher_id = input(f"Give the id of the teacher you want to "
                                   f"{'add' if add_or_remove == '1' else 'remove'}: ").strip()
                if not teacher_id.isdigit() or int(teacher_id) < 1:
                    teacher_id = input(f"Give the id of the teacher you want to "
                                       f"{'add' if add_or_remove == '1' else 'remove'} "
                                       f"(must be a positive integer): ").strip()
                teacher_id = int(teacher_id)

                if add_or_remove == "1":
                    teacher = teachers.read_teacher(teacher_id)
                    if teacher is None:
                        print("No teacher with the given id found in the database.")
                    elif teacher.teacher_id in self.read_lesson(lesson_id).teacher_ids:
                        print("Teacher is already in the lesson.")
                    else:
                        self.read_lesson(lesson_id).teacher_ids.append(teacher.teacher_id)
                        print("Teacher added to the lesson successfully.")
                else:
                    teacher = teachers.read_teacher(teacher_id)
                    if teacher is None:
                        print("No teacher with the given id found in the database.")
                    elif teacher.teacher_id not in self.read_lesson(lesson_id).teacher_ids:
                        print("Teacher already not in the lesson.")
                    else:
                        self.read_lesson(lesson_id).teacher_ids.remove(teacher.teacher_id)
                        print("Teacher removed from the lesson successfully.")

            else:
                add_or_remove = input("Do you want to add or remove a pupil (1 add, 2 remove): ").strip()
                while add_or_remove not in ["1", "2"]:
                    add_or_remove = input("Do you want to add or remove a pupil (1 add, 2 remove): ").strip()

                pupil_id = input(f"Give the id of the pupil you want to "
                                 f"{'add' if add_or_remove == '1' else 'remove'}: ").strip()
                if not pupil_id.isdigit() or int(pupil_id) < 1001:
                    pupil_id = input(f"Give the id of the pupil you want to "
                                     f"{'add' if add_or_remove == '1' else 'remove'} "
                                     f"(must be an integer > 1000): ").strip()
                pupil_id = int(pupil_id)

                if add_or_remove == "1":
                    pupil = pupils.search_pupil_by_id(pupil_id)
                    if pupil is None:
                        print("No pupil with the given id found in the database.")
                    elif pupil.pupil_id in self.read_lesson(lesson_id).pupil_ids:
                        print("Pupil is already in the lesson.")
                    else:
                        self.read_lesson(lesson_id).pupil_ids.append(pupil.pupil_id)
                        print("Pupil added to the lesson successfully.")
                else:
                    pupil = pupils.search_pupil_by_id(pupil_id)
                    if pupil is None:
                        print("No pupil with the given id found in the database.")
                    elif pupil.pupil_id not in self.read_lesson(lesson_id).pupil_ids:
                        print("Pupil is not in the lesson.")
                    else:
                        self.read_lesson(lesson_id).pupil_ids.remove(pupil.pupil_id)
                        print("Pupil removed from the lesson successfully.")
        else:
            print("No lesson with the given id found in the database.")

    def delete_lesson(self):
        lesson = self.read_lesson(self.input_lesson_id("delete"))

        if lesson is None:
            print("No lesson with the given id found in the database.")
        else:
            self.lessons.remove(lesson)
            print("Lesson deleted successfully.")