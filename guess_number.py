import random
number = random.randint(1,50)
max_attempts = 3
attempts = 0
print("WELCOME TO THE GUESSING GAME!!\n")
print("*******************************\n")
while attempts < max_attempts:
    guess = int(input("Guess the number(1,50): "))
    attempts +=1
    if guess == number:
       print(f"You win! Guess it in {attempts} tries")
       break
    elif guess < number:
       print("The number is too low")
    else:
       print("The number is too high")
if guess != number:
 print(f"Thank you for trying. The actual number is {number}")
