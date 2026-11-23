
# P7 - Student Management System with Classes
# VILA, KEVIN V.
# IV-BSIT C


class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.__grade = 0
        self.set_grade(grade)

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
            return True

        print("Invalid grade. Grade must be between 0 and 100.")
        return False

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.__grade:.2f}")


class Subject:
    def __init__(self, subject_name, subject_code):
        self.subject_name = subject_name
        self.subject_code = subject_code

    def display_subject(self):
        print(f"Subject: {self.subject_name}")
        print(f"Subject Code: {self.subject_code}")


class Section:
    def __init__(self, section_name, subject):
        self.section_name = section_name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_section(self):
        print("\n===== SECTION INFORMATION =====")
        print(f"Section: {self.section_name}")
        self.subject.display_subject()

        print("\n===== STUDENT LIST =====")

        for number, student in enumerate(self.students, start=1):
            print(f"\nStudent {number}")
            student.display_info()

        print(f"\nTotal students: {len(self.students)}")

    def update_student_grade(self, student_id, new_grade):
        for student in self.students:
            if student.student_id == student_id:
                if student.set_grade(new_grade):
                    print("Student grade updated successfully.")
                return

        print("Student ID not found.")


def main():
    subject = Subject("Python Programming", "ELEC4")
    section = Section("IV-BSIT C", subject)

    student1 = Student("2026-001", "Kevin Vila", 90)
    student2 = Student("2026-002", "Juan Dela Cruz", 85)
    student3 = Student("2026-003", "Mark Santos", 88)

    section.add_student(student1)
    section.add_student(student2)
    section.add_student(student3)

    print("STUDENT MANAGEMENT SYSTEM")
    section.display_section()

    print("\n===== UPDATE STUDENT GRADE =====")
    section.update_student_grade("2026-002", 92)

    section.display_section()


if __name__ == "__main__":
    main()
