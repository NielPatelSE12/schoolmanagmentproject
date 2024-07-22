import csv

class EditStudent:
    def __init__(self):
        pass

    def edit_student_by_id(self):
        # Ask the user for the student ID they want to edit
        student_id_to_edit = input("Enter the student ID to edit: ")

        #Read the existing data from the CSV file
        with open("student.csv", "r") as f:
            data = f.readlines()

        updated_data = []
        student_found = False

        # Go through each line in the CSV file
        for line in data:
            # Check if the line starts with the student ID we want to edit
            if line.strip() and line.startswith(student_id_to_edit):
                student_found = True
                # Display the current details of the student
                print("Current details:", line.strip().split(","))
                
                #  Ask the user for the new details
                new_legal_name = input("Enter new legal name: ")
                new_dob = input("Enter new DOB: ")
                new_address = input("Enter new address: ")
                new_grade_level = input("Enter new grade level: ")
                
                # Create the updated line with new details
                updated_line = f"{student_id_to_edit},{new_legal_name},{new_dob},{new_address},{new_grade_level}\n"
                updated_data.append(updated_line)
            else:
                # If this line is not the student we're editing, just keep it as is
                updated_data.append(line)

        #  If the student was found and updated, write the new data back to the CSV file
        if student_found:
            with open("student.csv", "w", newline='') as f:
                f.writelines(updated_data)
            print("Student details updated successfully.")
        else:
            print("Student ID not found.")
