name = input("Enter your name: ")
score = int(input("Enter your test score: "))

if score >= 90:
   grade = "A+"
elif score >= 80:
   grade = "B"
elif score >= 70:
   grade = "C+"
elif score >= 60:
   grade = "C"
elif score < 60:
   grade = "D"
else:
   print("Fail")

print(f"Student: {name}")
print(f"Score: {score}")
print(f"Grade: {grade}")

