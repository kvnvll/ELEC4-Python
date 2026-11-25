
# P8 - Inheritance and Polymorphism
# VILA, KEVIN V.
# IV-BSIT C


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def introduce(self):
        print("\n===== STUDENT INTRODUCTION =====")
        print(f"Hello, I am {self.name}.")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")


class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def introduce(self):
        print("\n===== TEACHER INTRODUCTION =====")
        print(f"Hello, I am {self.name}.")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Subject: {self.subject}")


def main():
    student1 = Student(
        "Kevin Vila",
        21,
        "2026-001",
        "BS Information Technology"
    )

    student2 = Student(
        "Juan Dela Cruz",
        20,
        "2026-002",
        "BS Information Technology"
    )

    teacher1 = Teacher(
        "Maria Santos",
        35,
        "T-101",
        "Python Programming"
    )

    teacher2 = Teacher(
        "Pedro Reyes",
        40,
        "T-102",
        "Database Management"
    )

    people = [student1, student2, teacher1, teacher2]



    print("===== PEOPLE INFORMATION =====")

    for person in people:
        person.introduce()


if __name__ == "__main__":
    main()
