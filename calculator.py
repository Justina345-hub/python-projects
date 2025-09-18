num1 = float(input("Enter a number:"))
operation = input("Enter an operation to perfrom(+,-,*,/,%,**):")
num2 = float(input("ennter another number:"))
if operation == "+":
    result == num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result  = num1 * num2 
elif operation == "/":
      result = num1 / num2 if num2 != 0 else "not divisble by zero"
elif operation == "%":
    result = num1 /num2 if num2 != 0 else "not divisble by zero"
elif operation == "**":
    result = num1 ** num2
else:
    result = "invalid operator"
print(f"{num1} {operation} {num2} = { result}")


