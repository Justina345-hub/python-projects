"""
========================================================================
MY STUDENT ACADEMIC RECORD MANAGEMENT SYSTEM (PYTHON)
========================================================================

========================
PART A: ASSIGNMENT DESCRIPTION
========================

Title: Student Academic Record Management System

Author: Justina Mwango
Date: 02-Feb-2026
Course: Software Engineering 101

Objective:
This Python program allows students’ academic records to be stored,
managed, and analyzed. It provides practice in:

- Using nested dictionaries to store structured data
- Implementing loops and conditional logic for program flow
- Writing and organizing functions for modularity
- Validating user input to prevent errors
- Calculating totals, averages, and grades
- Generating simple, readable reports

Description:
The system enables users to:

1. Add new student records with multiple subjects and marks
2. View a list of all students
3. Display detailed student reports including total marks, average, and grade
4. Update marks for existing subjects
5. Delete student records
6. Exit the program

Data Structure:
Student information is stored in nested dictionaries. Each student ID
acts as a key, and its value is another dictionary containing the student's
name, class, and subject marks.
"""
# =========================
# GLOBAL STUDENT STORAGE
# =========================
students = {}


# =========================
# GRADE CALCULATION
# =========================
def calculate_grade(avg):
    return 'A' if avg >= 85 \
    else 'B' if avg >= 70 \
    else 'C' if avg >= 55 \
    else 'D' if avg >= 40 \
    else 'F'



# =========================
# ADD STUDENT
# =========================
def register_new_student():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter Full Name: ")
    class_name = input("Enter Class: ")

    subjects = {}

    for i in range(3):
        subject = input(f"Enter subject {i+1} name: ")

        while True:
            try:
                mark = int(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

        subjects[subject] = mark

    students[student_id] = {
        "name": name,
        "class": class_name,
        "subjects": subjects
    }

    print("Student added successfully.")


# =========================
# VIEW ALL STUDENTS
# =========================
def display_all_students():
    if not students:
        print("No student records available.")
        return

    print("\n--- ALL STUDENTS ---")
    for student_id, details in students.items():
        print(f"ID: {student_id} | Name: {details['name']}")


# =========================
# VIEW STUDENT REPORT
# =========================
def show_student_report():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]
    subjects = student["subjects"]

    total = sum(subjects.values())
    avg = total / len(subjects)
    grade = calculate_grade(avg)

    print("\n--- STUDENT REPORT ---")
    print("Name:", student["name"])
    print("Class:", student["class"])

    print("Subjects and Marks:")
    for subject, mark in subjects.items():
        print(f"{subject}: {mark}")

    print("Total Marks:", total)
    print("Average:", round(avg, 2))
    print("Grade:", grade)


# =========================
# UPDATE MARKS
# =========================
def modify_grade():
    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    subject = input("Enter subject name to update: ")

    if subject not in students[student_id]["subjects"]:
        print("Subject not found.")
        return

    while True:
        try:
            new_mark = int(input("Enter new marks (0 being the lowest 100 being the higest): "))
            if 0 <= new_mark <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Enter a valid number.")

    students[student_id]["subjects"][subject] = new_mark
    print("Marks updated successfully.")


# =========================
# DELETE STUDENT
# =========================
def remove_student():
    student_id = input("Enter Student ID you want to remove: ")

    if student_id in students:
        del students[student_id]
        print("Student record deleted.")
    else:
        print("Student not found.")


# =========================
# MAIN MENU
# =========================
def main_menu():
    while True:
        print("""
==============================
STUDENT MANAGEMENT MENU
==============================
1. Register New Student
2. Display All Students
3. Show Student Report
4. Modify Grades
5. Remove Student
6. Exit
""")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            register_new_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            show_student_report()
        elif choice == "4":
            modify_grade()
        elif choice == "5":
            remove_student()
        elif choice == "6":
            print("Program Existed. Thank You For Using Our System ")
            break
        else:
            print("Invalid choice. Try again.")


# =========================
# PROGRAM ENTRY POINT
# =========================
main_menu()  