
# Name: VILA, KEVIN V.
# Section: IV-BSIT C
# Activity: P4 - Safe Menu Program
# Date: November 2026

def division():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        result = first_number / second_number

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    except ZeroDivisionError:
        print("Error! You cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation finished.")


def open_file():
    filename = input("Enter the filename to open: ").strip()

    try:
        file = open(filename, "r")
        content = file.read()

    except FileNotFoundError:
        print("Error! File not found.")

    except PermissionError:
        print("Error! You don't have permission to open this file.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(content)
        file.close()

    finally:
        print("File operation finished.")


def main():
    while True:
        print("\n===== SAFE MENU PROGRAM =====")
        print("1. Division")
        print("2. Open a File")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Invalid input! Please enter a number from 1 to 3.")
            continue

        if choice == 1:
            division()

        elif choice == 2:
            open_file()

        elif choice == 3:
            print("Program closed. Goodbye!")
            break

        else:
            print("Invalid menu choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
