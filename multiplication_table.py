number = int(input("Enter a number: "))
for i in range(1,11):
   print(f"{number} x {i} = {number*i}")


for n in range(1,6):
   print(f"\nTable of {n}")
   for i in range(1,11):
       print(f"{n} x {i} = {n*i}")
