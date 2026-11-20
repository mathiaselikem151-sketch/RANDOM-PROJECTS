import random

option1 = "rock"
option2 = "paper"
option3 = "scissors"
main = (option2, option3, option1)
computer = random.choice(main)
is_running = True
print("========= Rock - Paper - Scissors - Game =========")
while is_running:
    guess = input("Enter your choice: ").lower
    if guess == option1:
        if computer == guess:
            print()
            print(f"Your answer: {guess}")
            print(f"Computer: {computer}")
            print("You both have the same answer, Try again")
        elif computer == option2:
            print()
            print(f"Your answer: {guess}")
            print(f"Computer: {computer}")
            print("Sorry,You lost to computer, Try again")
        elif computer == option3:
            print()
            print(f"Your answer: {guess}")
            print(f"Computer: {computer}")
            print("Congrats!!, You won")
            is_running  = True

    elif guess == option2:  #paper
        if computer == guess:
            print()
            print(f"Your answer: {guess}")
            print(f"Computer: {computer}")
            print("You both have the same answer, Try again")
        elif computer == option1: #rock
            print()
            print(f"Your answer: {guess}")
            print(f"Computer: {computer}")
            print("Congrats!!, You won")
            is_running = True
        elif computer == option3:
            print()
            print(f"Your answer: {guess}")
            print(f"Computer: {computer}")
            print("Sorry,You lost to computer, Try again")

    elif guess == option3:  #scissors
        if computer == guess:
            print()
            print(f"Your answer: {guess}")
            print(f"Computer: {computer}")
            print("You both have the same answer, Try again")
        elif computer == option1: #rock
            print()
            print(f"Your answer: {guess}")
            print(f"Computer: {computer}")
            print("Sorry,You lost to computer, Try again")
            is_running = True
        elif computer == option2: #paper
            print()
            print(f"Your answer: {guess}")
            print(f"Computer: {computer}")
            print("Congrats!!, You won")
else:
    print()
    print("Invalid!!")
    guess = input("Enter your choice again, (ROCK, PAPER, SCISSORS): ")

print()
print("Good Game, thx fo rparticipating")