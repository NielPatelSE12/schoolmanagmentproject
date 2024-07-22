import csv

class CreateStudent:
    def __init__(self, student_id, legal_name, dob, address, grade_level):
        self.__student_id = student_id
        self.__legal_name = legal_name
        self.__dob = dob
        self.__address = address
        self.__grade_level = grade_level

    def student_list(self):
        return [self.__student_id, self.__legal_name, self.__dob, self.__address, self.__grade_level]

def get_student_input():
    student_id = input("Enter student's new ID: ")
    legal_name = input("Enter student's legal name: ")
    dob = input("Enter student's DOB: ")
    address = input("Enter student's address: ")
    grade_level = input("Enter student's grade level: ")
    return CreateStudent(student_id, legal_name, dob, address, grade_level)

def save_student_to_csv(student):
    with open('student.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student.student_list())
