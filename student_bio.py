students = []
def add_student():
  for i in range(5):
        print(f"\nEnter student details{i + 1}: ")
        name = input("Enter student name: ") 
        age = int(input("Enter student's age: "))
        course = input("Enter students's course: ")


        student = {
               "Name": name,
               "Age": age,
               "Course": course
 
               }

        students.append(student)

add_student()

print("\n---Student Bio---")
for student in students:
    print(f"\nStudent Name: {student['Name']}")
    print(f"Age: {student['Age']}")
    print(f"Course: {student['Course']}")

