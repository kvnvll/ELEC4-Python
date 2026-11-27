
# Name: VILA, KEVIN V.
# Section: IV-BSIT C
# Activity: P3 - Student Record Manager
# Date: November 2026

# A list stores student names and keeps their original order.
# A set stores unique values and does not allow duplicate elements.
# Lists can contain duplicate names, while sets automatically prevent duplicates.
# Lists are useful for displaying and managing records, while sets help check duplicates quickly.

student_names = []
student_set = set()


def add_student(student_names, student_set):
    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    if name.lower() in student_set:
        print("Student already exists!")
    else:
        student_names.append(name)
        student_set.add(name.lower())
        print("Student added successfully!")


def remove_student(student_names, student_set):
    name = input("Enter student name to remove: ").strip()

    for student in student_names:
        if student.lower() == name.lower():
            student_names.remove(student)
            student_set.remove(student.lower())
            print("Student removed successfully!")
            return

    print("Student not found!")


def search_student(student_names):
    name = input("Enter name to search: ").strip().lower()

    if name == "":
        print("Please enter a name to search.")
        return

    found_students = []

    for student in student_names:
        if name in student.lower():
            found_students.append(student)

    if found_students:
        print("\n===== SEARCH RESULTS =====")

        for i, student in enumerate(found_students, start=1):
            print(f"{i}. {student}")

        print("Total found:", len(found_students))
    else:
        print("No matching student found.")


def display_students(student_names):
    if not student_names:
        print("\nNo student records available.")
        return

    sorted_students = sorted(student_names, key=str.lower)

    print("\n===== STUDENT RECORDS =====")

    for i, student in enumerate(sorted_students, start=1):
        print(f"{i}. {student}")

    print("---------------------------")
    print("Total Students:", len(student_names))


def display_menu():
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(student_names, student_set)

        elif choice == "2":
            remove_student(student_names, student_set)

        elif choice == "3":
            search_student(student_names)

        elif choice == "4":
            display_students(student_names)

        elif choice == "5":
            print("\nThank you for using Student Record Manager!")
            break

        else:
            print("Invalid choice! Please select from 1 to 5.")


if __name__ == "__main__":
    main()
