import csv

FILE_NAME = "students.csv"

# 1. Add Student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, age, course])

    print("Student Added Successfully!\n")


# 2. View Students
def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- Student List ---")
            for row in reader:
                print(f"Roll: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
    except FileNotFoundError:
        print("No file found!\n")


# 3. Search Student
def search_student():
    roll_no = input("Enter Roll No to search: ")
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == roll_no:
                    print(f"Student Found: {row}")
                    found = True
                    break

        if not found:
            print("Student not found!\n")

    except FileNotFoundError:
        print("No file found!\n")


# 4. Delete Student
def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    rows = []
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != roll_no:
                    rows.append(row)
                else:
                    found = True

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        if found:
            print("Student Deleted Successfully!\n")
        else:
            print("Student not found!\n")

    except FileNotFoundError:
        print("No file found!\n")


# Main Menu
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid Choice!\n")


main()