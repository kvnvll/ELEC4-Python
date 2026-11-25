
# P5 - Student Information File System
# VILA, KEVIN V.
# IV-BSIT C

import os

FILE_NAME = "students.txt"


def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    student = {
                        "id": data[0],
                        "name": data[1],
                        "course": data[2],
                        "average": float(data[3])
                    }
                    students.append(student)

    except FileNotFoundError:
        print("Student file not found. A new file will be created.")

    except ValueError:
        print("Some records contain invalid average values.")

    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(
                f"{student['id']}|{student['name']}|"
                f"{student['course']}|{student['average']}\n"
            )


def add_student(students):
    student_id = input("Enter Student ID: ").strip()

    if any(student["id"] == student_id for student in students):
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course and Section: ").strip()

    try:
        average = float(input("Enter Average Grade: "))

        if average < 0 or average > 100:
            print("Average must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    students.append({
        "id": student_id,
        "name": name,
        "course": course,
        "average": average
    })

    save_students(students)
    print("Student added successfully.")


def display_students(students):
    if not students:
        print("No student records found.")
        return

    print("\nSTUDENT RECORDS")

    for student in students:
        print("-------------------------")
        print("Student ID:", student["id"])
        print("Name:", student["name"])
        print("Course and Section:", student["course"])
        print("Average:", student["average"])


def search_student(students):
    student_id = input("Enter Student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print("Course and Section:", student["course"])
            print("Average:", student["average"])
            return

    print("Student not found.")


def update_student(students):
    student_id = input("Enter Student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Student found.")
            print("Leave the field blank to keep its current value.")

            name = input("New Name: ").strip()
            course = input("New Course and Section: ").strip()
            average_input = input("New Average: ").strip()

            if name:
                student["name"] = name

            if course:
                student["course"] = course

            if average_input:
                try:
                    average = float(average_input)

                    if 0 <= average <= 100:
                        student["average"] = average
                    else:
                        print("Invalid average. Previous average kept.")

                except ValueError:
                    print("Invalid number. Previous average kept.")

            save_students(students)
            print("Student record updated.")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\nSTUDENT INFORMATION FILE SYSTEM")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()