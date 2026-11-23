
# Name: VILA, KEVIN V.
# Section: IV-BSIT C
# Activity: P1 - Student Grade Calculator
# Date: November 2026


# Global variable: This variable can be accessed by different functions in the program.
# It stores the grades entered by the user.
# Local variables are created inside functions and can only be used within those functions.
# Using local variables helps prevent unnecessary changes to data outside a function.


def enter_grades():
    student_grades = []

    while True:
        try:
            number_of_grades = int(input("How many grades do you want to enter? "))

            if number_of_grades > 0:
                break
            else:
                print("Please enter at least one grade.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    for i in range(number_of_grades):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    student_grades.append(grade)
                    break
                else:
                    print("Invalid grade! Enter a grade from 0 to 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    return student_grades


def calculate_average(grades):
    average = sum(grades) / len(grades)
    return average


def get_highest(grades):
    highest = max(grades)
    return highest


def get_lowest(grades):
    lowest = min(grades)
    return lowest


def check_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


def display_results(grades):
    if len(grades) == 0:
        print("\nNo grades available. Please enter grades first.")
        return

    average = calculate_average(grades)
    highest = get_highest(grades)
    lowest = get_lowest(grades)
    status = check_status(grades)

    print("\n===== STUDENT GRADE RESULTS =====")
    print("Grades:", grades)
    print("Average Grade:", round(average, 2))
    print("Highest Grade:", highest)
    print("Lowest Grade:", lowest)
    print("Status:", status)


def display_menu():
    print("\n===== STUDENT GRADE CALCULATOR =====")
    print("1. Enter Grades")
    print("2. View Results")
    print("3. Exit")


# Main program
grades = []

while True:
    display_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        grades = enter_grades()
        print("\nGrades successfully saved!")

    elif choice == "2":
        display_results(grades)

    elif choice == "3":
        print("\nThank you for using the Student Grade Calculator!")
        break

    else:
        print("\nInvalid choice! Please select 1, 2, or 3.")
