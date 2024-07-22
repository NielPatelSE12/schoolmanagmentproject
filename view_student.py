import create_new_student

class ViewStudentProfile:
    def __init__(self):
        #opening student.csv file for read mode
        self.studentFile = open("student.csv", "r+")
    #function for displaying students in the file
    def view_student_profile(self):
        print("Students:")
        print(self.studentFile.read())
        print()
        self.studentFile.close()
