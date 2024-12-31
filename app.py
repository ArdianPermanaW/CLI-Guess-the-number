import random

print('''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
      
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
''')

diff = int(input("difficulty level: "))
chances = 0
match diff:
    case 1:
        chances = 10
    case 2:
        chances = 5
    case 3:
        chances = 3
    case _:
        print("bro are you stupid it says 1, 2 and 3 yk what im gonna default it to hard")
        chances = 3
        

print(f"You have {chances} chances to guess the correct number. \nLet's start the game!\n")

ans = random.randint(1,100)
attempt = 1
while chances > 0:
    guess = int(input("Enter your guess: "))
    if guess == ans:
        print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
    elif guess > ans:
        print(f"Incorrect! The number is less than {guess}.\n")
    else:
        print(f"Incorrect! The number is more than {guess}.\n")
    chances -= 1
    attempt += 1

print("U lost womp womp, better luck next time")
