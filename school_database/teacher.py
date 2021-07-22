class Teacher:
    def __init__(self, first_name="", last_name="", teacher_id=1):
        self.first_name = first_name
        self.last_name = last_name
        self.teacher_id = teacher_id

    def from_dict(self, teacher):
        self.first_name = teacher["first_name"]
        self.last_name = teacher["last_name"]
        self.teacher_id = teacher["teacher_id"]

    def to_dict(self):
        return {"first_name": self.first_name, "last_name": self.last_name, "teacher_id": self.teacher_id}

    def print_teacher(self):
        print(f"First name: {self.first_name}")
        print(f"Last name:\t {self.last_name}".expandtabs(11))
        print(f"Teacher id: {self.teacher_id}")
