#Python guessing Game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0

print(f"Select a number between {lowest_num} and {highest_num} ")
guess = input("Enter your number: ")

is_running = True

while is_running:
    if guess.isdigit():
        guess = int(guess)
        if guess < lowest_num or guess > highest_num:
            print()
            print(f"Invalid")
            print(f"Select a number between {lowest_num} and {highest_num} ")
            guess = input("Enter your number: ")

        elif guess < answer:
            print()
            print("Its too low, try again!")
            guess = input("Enter your number: ")
            guesses += int(guess)

        elif guess > answer:
            print()
            print("Its too high, try again")
            guess = input("Enter your number: ")
            guesses += int(guess)

        else:
            print()
            print("Correct!!")
            print(f"Number of guess: {guesses}")
            is_running = False
    else:
        print()
        print("Invalid!!")
        print(f"Select a number between {lowest_num} and {highest_num} ")
        guess = input("Enter your number: ")