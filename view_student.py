import create_new_student

class ViewStudentProfile:
    def __init__(self):
        self.studentFile = open("student.csv", "r+")

    def view_student_profile(self):
        print("Students:")
        print(self.studentFile.read())
        print()
        self.studentFile.close()
