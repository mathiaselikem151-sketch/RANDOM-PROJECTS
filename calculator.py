import math
from operator import truediv

is_running = True
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
opp = input("Enter your operator (+, /, *, -):")

while is_running:
    print()
    print("====================CALCULATOR=====================")

    if opp == "+":
        print("======= ADDITION ======= ")
        add = num2 + num1
        print(f" Your answer is: {add}")
        print()
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        opp = input("Enter your operator (+, /, *, -) else press quit to quit:")
        if opp == "q":
            is_running = False
        else:
           is_running
        print("======================== ")

    elif opp == "-":
        print("======= SUBTRACTION ======= ")
        add = num1 - num2
        print(f" Your answer is: {add}")
        print()
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        opp = input("Enter your operator (+, /, *, -) else press quit to quit:")
        if opp == "q":
            is_running = False
        else:
            is_running
        print("======================== ")

    elif opp == "/":
        print("======= DIVISION ======= ")
        add = num1 / num2
        print(f" Your answer is: {add}")
        print()
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        opp = input("Enter your operator (+, /, *, -) else press quit to quit:")
        if opp == "q":
            is_running = False
        else:
            is_running
        print("======================== ")

    elif opp == "+":
        print("======= MULTIPLICATION ======= ")
        add = num2 * num1
        print(f" Your answer is: {add}")
        print()
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        opp = input("Enter your operator (+, /, *, -) else press quit to quit:")
        if opp == "q":
            is_running = False
        else:
            is_running
        print("======================== ")