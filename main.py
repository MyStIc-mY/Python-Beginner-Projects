import random
secret_number=random.randint(1,100)
attempts=10
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100")
print("You will be given total 10 attempts to guess the number.")
b="LET START"

print(b.center(50))

while attempts>=0:
   
    
   
    a=int(input("enter your guess:"))
    
    if a<secret_number:
        print("You Guessed a incorrect number")
        print("Your number is low from guessed number")
        print("You have",attempts,"attempts left")
    elif a>secret_number:    
        print("You Guessed a incorrect number")
        print("Your number is high from guessed number")
        print("You have", attempts,"attempts left")
    else:
        print("Congratulations! You guessed the correct number:",secret_number)
        break
    if attempts==0:
        print("Sorry, you've used all your attempts. The correct number was:",secret_number)
        break
    attempts=attempts-1