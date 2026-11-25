
# Name: VILA, KEVIN V.
# Section: IV-BSIT C
# Activity: P2 - Custom Module
# Date: November 2026

import student_utils
from student_utils import pass_fail
from datetime import datetime


def main():
    grades = []

    print("===== STUDENT GRADE SYSTEM =====")

    while True:
        try:
            number = int(input("How many grades do you want to enter? "))

            if number > 0:
                break
            else:
                print("Please enter at least one grade.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    for i in range(number):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    print("\n===== STUDENT GRADE RESULTS =====")

    print("Report Date:", datetime.now().strftime("%B %d, %Y"))
    print("Grades:", grades)
    print("Average:", round(student_utils.average(grades), 2))
    print("Highest Grade:", student_utils.highest(grades))
    print("Lowest Grade:", student_utils.lowest(grades))
    print("Status:", pass_fail(grades))


if __name__ == "__main__":
    main()
