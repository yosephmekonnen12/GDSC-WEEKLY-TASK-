def add_student(database):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    # Add any other relevant details you want to collect
    
    database[name] = {
        'age': age,
        'grade': grade
        # Add other details here
    }
    print("Student added successfully!")


def view_student(database):
    name = input("Enter student name: ")
    if name in database:
        student = database[name]
        print("Name:", name)
        print("Age:", student['age'])
        print("Grade:", student['grade'])
        # Print other details here
    else:
        print("Student not found in the database.")


def list_all_students(database):
    if not database:
        print("No students in the database.")
    else:
        for name, student in database.items():
            print("Name:", name)
            print("Age:", student['age'])
            print("Grade:", student['grade'])
            # Print other details here


def update_student(database):
    name = input("Enter student name: ")
    if name in database:
        student = database[name]
        print("Current Information:")
        print("Name:", name)
        print("Age:", student['age'])
        print("Grade:", student['grade'])
        # Print other details here
        
        age = input("Enter new age (press enter to skip): ")
        if age:
            student['age'] = age
        
        grade = input("Enter new grade (press enter to skip): ")
        if grade:
            student['grade'] = grade
        
        print("Student information updated successfully!")
    else:
        print("Student not found in the database.")


def delete_student(database):
    name = input("Enter student name: ")
    if name in database:
        del database[name]
        print("Student deleted successfully!")
    else:
        print("Student not found in the database.")


def main():
    database = {}
    
    while True:
        print("\n===== Student Database Program =====")
        print("1. Add Student")
        print("2. View Student")
        print("3. List All Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("0. Exit")
        
        choice = input("Enter your choice (0-5): ")
        
        if choice == '1':
            add_student(database)
        elif choice == '2':
            view_student(database)
        elif choice == '3':
            list_all_students(database)
        elif choice == '4':
            update_student(database)
        elif choice == '5':
            delete_student(database)
        elif choice == '0':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
