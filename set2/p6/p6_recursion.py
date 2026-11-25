
# P6 - Recursion Toolkit
# VILA, KEVIN V.
# IV-BSIT C


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def display_fibonacci(n, current=0):
    if current >= n:
        return

    print(fibonacci(current), end=" ")
    display_fibonacci(n, current + 1)


def sum_numbers(n):
    if n <= 0:
        return 0

    return n + sum_numbers(n - 1)


def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return -1

    if numbers[index] == target:
        return index

    return recursive_search(numbers, target, index + 1)


def main():
    while True:
        print("\nRECURSION TOOLKIT")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Sum of Numbers")
        print("4. Recursive List Search")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                number = int(input("Enter a number: "))

                if number < 0:
                    print("Please enter a non-negative number.")
                else:
                    print("Factorial:", factorial(number))

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":
            try:
                number = int(input("Enter the number of terms: "))

                if number <= 0:
                    print("Please enter a number greater than zero.")
                else:
                    print("Fibonacci Series:")
                    display_fibonacci(number)
                    print()

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "3":
            try:
                number = int(input("Enter a positive number: "))

                if number < 0:
                    print("Please enter a non-negative number.")
                else:
                    print("Sum:", sum_numbers(number))

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "4":
            try:
                numbers = list(map(int, input(
                    "Enter numbers separated by spaces: "
                ).split()))

                target = int(input("Enter the number to search: "))

                result = recursive_search(numbers, target)

                if result == -1:
                    print("Number not found.")
                else:
                    print("Number found at index:", result)

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()