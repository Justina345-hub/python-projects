def calculate_grade(mark):
  if mark >= 90:
    return 'A', 'Distinction'
  elif mark >=80:
    return 'B', 'Merit'
  elif mark >= 70:
    return 'C', 'Credit'
  elif mark >= 60:
    return 'D', 'Pass'
  else:
    return 'F', 'Fail'


students={
"Alice": 95,
"Bob": 82,
"Charlie": 67,
"David": 74,
"Eva": 89
}
for name, mark in students.items():
  grade,message = calculate_grade(mark)
  print(f"{name}:{mark} - Grade {grade} ({message})")
