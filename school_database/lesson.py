class Lesson:
    def __init__(self, lesson_name="", lesson_id=10001):
        self.lesson_name = lesson_name
        self.teacher_ids = []
        self.pupil_ids = []
        self.lesson_id = lesson_id

    def from_dict(self, lesson):
        self.lesson_name = lesson["lesson_name"]
        self.teacher_ids = lesson["teachers"]
        self.pupil_ids = lesson["pupils"]
        self.lesson_id = lesson["lesson_id"]

    def to_dict(self):
        return {"lesson_name": self.lesson_name, "teachers": self.teacher_ids, "pupils": self.pupil_ids,
                "lesson_id": self.lesson_id}

    def to_string(self, teachers, pupils):
        string = f"Lesson name: {self.lesson_name}\n"
        string += f"Lesson id:\t {self.lesson_id}\n\n".expandtabs(12)
        string += f"Teachers:\n"
        string += "\n".join([f"\t{teachers.read_teacher(teacher_id).first_name} "
                             f"{teachers.read_teacher(teacher_id).last_name}, "
                             f"ID = {teacher_id}" for teacher_id in self.teacher_ids]) \
            if len(self.teacher_ids) > 0 else "\tThis lesson has no teachers."
        string += f"\n\nPupils:\n"
        string += "\n".join([f"\t{pupils.search_pupil_by_id(pupil_id).first_name} "
                             f"{pupils.search_pupil_by_id(pupil_id).last_name}, "
                             f"ID = {pupil_id}" for pupil_id in self.pupil_ids]) \
            if len(self.pupil_ids) > 0 else "\tThis lesson has no pupils."
        return string
