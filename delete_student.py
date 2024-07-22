import create_new_student

class DeleteStudent:
    def __init__(self):
        #creating the instance 
        self.delete_student_by_id()
    # Getting the student id to be able to delete the student profile
    def delete_student_by_id(self):
        student_id_to_delete = input("Enter the student ID to delete:")
        #Opening the file
        with open("student.csv","r") as f:
            data = f.readlines()
    #Read the line to find the student id that matches what the user has provided.
        with open("student.csv","w",newline="") as f:
            for line in data:
                if line.strip() and not line.startswith(student_id_to_delete):
                    f.write(line)

               


