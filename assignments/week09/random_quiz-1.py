"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random

def test_random():
    random_number = random.randint(1, 20)
    print("โปรเเกรมทายเลข 1-20")
    for i in range(6):
        Totalrandom = int(input("EnterNumber ="))   
        if random_number == Totalrandom:
            print("correct")
            break
        elif random_number > Totalrandom:
            print(f"อาจะยังน้า น้อยไปนิดนึง ครั้งที่{i+1}")   
        elif random_number < Totalrandom:
            print(f"อาจจะยังน้า มากไปนิดนิง ครี่งที่{i+1}")
    print(random_number)   
test_random()