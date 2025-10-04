# Student Management System with Admin and Student Roles

admin_username = "Ahmad"
admin_password = "Ahmad123"

STUDENT_FILE = "students.txt"
MARKS_FILE = "marks.txt"


def admin_menu():
    while True:
        print("--- Admin Menu ---\n")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Enter Marks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            enter_marks()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
  

def student_menu(username):
    while True:
        print("--- Student Menu ---\n")
        print("1. View Profile")
        print("2. View Marks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(username)
        elif choice == "2":
            view_marks(username)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")


def add_student():
    username = input("Enter student username: ")
    password = input("Enter student password: ")
    name = input("Enter student name: ")
    department = input("Enter department: ")

    with open(STUDENT_FILE, "a") as f:
        f.write(f"{username},{password},{name},{department}\n")
    print("Student added successfully!")


def view_students():
    print("\n--- All Students ---")
    try:
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                data = line.strip().split(",")
                print("Username:", data[0], "| Name:", data[2], "| Dept:", data[3])
    except FileNotFoundError:
        print("No students found.")


def enter_marks():
    username = input("Enter student username: ")
    course = input("Enter course name: ")
    try:
        marks = int(input("Enter marks (out of 100): "))
    except ValueError:
        print("Invalid marks. Please enter a number.")
        return

    if marks >= 85:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    with open(MARKS_FILE, "a") as f:
        f.write(f"{username},{course},{marks},{grade}\n")
    print("Marks entered successfully!")


def view_profile(username):
    try:
        with open(STUDENT_FILE, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == username:
                    print("Username:", data[0])
                    print("Name:", data[2])
                    print("Department:", data[3])
                    return
        print("Profile not found.")
    except FileNotFoundError:
        print("No student data found.")


def view_marks(username):
    found = False
    try:
        with open(MARKS_FILE, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == username:
                    print("Course:", data[1], "| Marks:", data[2], "| Grade:", data[3])
                    found = True
        if not found:
            print("No marks found.")
    except FileNotFoundError:
        print("No marks data found.")


def login():
    print("\n--- Login ---")
    role = input("Select Role (1-Admin, 2-Student): ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if role == "1":

        if username == admin_username and password == admin_password:
            admin_menu()
        else:
            print("Invalid admin credentials.")
    elif role == "2":
        
        try:
            with open(STUDENT_FILE, "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if data[0] == username and data[1] == password:
                        student_menu(username)
                        return
            print("Invalid student credentials.")
        except FileNotFoundError:
            print("No student records found.")
    else:
        print("Invalid role selected.")


while True:
    print("\n===== Student Management System =====")
    login()
    again = input("Do you want to continue? (y/n): ")
    if again.lower() != 'y':
        break
