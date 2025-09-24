students = {}

for i in range(5):
  name = input(f"Enter student {i +1} name: ")
  mark = int(input(f"Enter {name}'s mark: "))
  students[name] = mark


def assign_grade(mark):
  return(
    'A' if mark >= 90 else
    'B' if mark >= 80 else
    'C' if mark >= 70 else
    'D' if mark >= 60 else
    'F'
)

total = 0
for name, mark in students.items():
  grade = assign_grade(mark)
  total += mark
  print(f"{name}: {mark} - Grade {grade}")

average = total/len(students)
print(f"Average marks: {average:.1f}")
