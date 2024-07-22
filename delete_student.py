import create_new_student

class DeleteStudent:
    def __init__(self):
        self.delete_student_by_id()

    def delete_student_by_id(self):
        student_id_to_delete = input("Enter the student ID to delete:")
        
        with open("student.csv","r") as f:
            data = f.readlines()

        with open("student.csv","w",newline="") as f:
            for line in data:
                if line.strip() and not line.startswith(student_id_to_delete):
                    f.write(line)

               


