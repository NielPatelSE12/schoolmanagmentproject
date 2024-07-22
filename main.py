import create_new_student
import delete_student
import edit_student
import view_student
import time

menu_options = ("1", "2", "3", "4")

while True:
    print()
    print("** WELCOME TO THE MAIN MENU **")

    print("1 = Create New Student")
    print("2 = Edit Student")
    print("3 = Delete Student")
    print("4 = View Student")
    
    print()
    user_input = input("Enter an option using the numbers:")

    if user_input in menu_options:
        if user_input == "1":
            student = create_new_student.get_student_input()
            create_new_student.save_student_to_csv(student)
            print("Student was created and saved successfully")
        elif user_input == "2":
            edit_student_instance = edit_student.EditStudent()
            edit_student_instance.edit_student_by_id()
        elif user_input == "3":
            delete_student_instance = delete_student.DeleteStudent()
            delete_student_instance.delete_student_by_id()
            print("Student was deleted successfully")
        elif user_input == "4":
            view_student_instance = view_student.ViewStudentProfile()
            view_student_instance.view_student_profile()
        break
    else:
        print()
        print("OPTION NOT AVAILABLE")
