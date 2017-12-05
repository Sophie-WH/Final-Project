# Final Project
# The plan-- create a series of math games the user can play involving multiplication, division, addition, and subtraction

import time
import random
import os

MULTIPLICATION_CHOICE = 1
DIVISION_CHOICE= 2
ADDITION_CHOICE = 3
SUBTRACTION_CHOICE = 4
RANDOM_CHOICE = 5
QUIT_CHOICE = 6

def main():
    
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        try:
            choice = int(input("Please enter the number of your choice: "))
        except:
            os.system("printf '\033c'")
            print("\nPlease enter an actual number.")
        handle_choice(choice)
        
def handle_difficulty():
    
    thisistrue = False
    
    print("Please enter the level of difficulty you would like:")
    print("\n1) Easy")
    print("2) Medium")
    print("3) Hard")
    
    while thisistrue == False:
        try:
            number = int(input("4) I want to set my own number of problems!\n\n"))
            thisistrue = True
            if number == 1:
                problems = [0] * 5
                return problems
            if number == 2:
                problems = [0] * 7
                return problems
            if number == 3:
                problems = [0] * 10
                return problems
            if number == 4:
                difficulty = int(input("Please enter your number of problems: "))
                problems = [0] * difficulty
                return problems
            else:
                raise Exception("Number out of bounds!")
        except:
            os.system("printf '\033c'")
            thisistrue = False
            print("Please enter an actual number.")
            print("Please enter the level of difficulty you would like:")
            print("\n1) Easy")
            print("2) Medium")
            print("3) Hard")
        
def instructions():
    print("\nGreat! You will have thirty seconds to answer all of the problems.")
    time.sleep(2)
    print("Ready?")
    time.sleep(1)
    print("Set...")
    time.sleep(1)
    print("GO!\n")
    time.sleep(1)
    
def check_answers(num_of_problems, given_answers, problems, starttime, endtime):
    
    print("\nChecking answers...\n")
    
    time.sleep(1)
    
    correctanswers = 0
    
    for x in range(0, int(num_of_problems)):
        if given_answers[x] == str(problems[x]):
            correctanswers += 1
            
    if correctanswers == num_of_problems and round(endtime - starttime) < 30:
        print("You got all the problems correct in less than thirty seconds! You win!")
        time.sleep(4)
        os.system("printf '\033c'")
    elif correctanswers == num_of_problems and round(endtime - starttime) > 30:
        print("All your answers were correct, but you did not do it in under thirty seconds. You lose.")
        time.sleep(4)
        os.system("printf '\033c'")
    else:
        print("Your answers were incorrect. You lose.")
        time.sleep(4)
        os.system("printf '\033c'")
        
def handle_multiplication():
    
    print("Welcome to Multiplying Mania!")
    
    problems = handle_difficulty()
    num_of_problems = len(problems)
    time.sleep(2)
    
    os.system("printf '\033c'")
    instructions()
    
    starttime = time.time()
    for x in range(0, int(num_of_problems)):
        int1 = random.randint(1, 10)
        int2 = random.randint(1, 10)
        problems[x] = int1 * int2
        print(str(int1) + " x " + str(int2))
    
    given_answers = [0] * len(problems)
    for x in range(0, int(num_of_problems)):
        answer = input("Question " + str(x + 1) + ": ")
        given_answers[x] = answer
    endtime = time.time()
    if num_of_problems > len(given_answers):
        for x in range(0, num_of_problems - len(given_answers)):
            given_answers.append(0)
            
    correctanswers = 0
    
    time.sleep(1)
    check_answers(num_of_problems, given_answers, problems, starttime, endtime)
        
def handle_division():
    
    print("Welcome to Devilish Dividing!")
    
    problems = handle_difficulty()
    num_of_problems = len(problems)
    time.sleep(2)
    
    os.system("printf '\033c'")
    instructions()
    starttime = time.time()
    for x in range(0, int(num_of_problems)):
        int1 = random.randint(1, 50)
        int2 = random.randint(2, 5)
        mod = False
        while mod == False:
            if int1 % int2 == 0:
                mod = True
            else:
                int1 = random.randint(1, 50)
                int2 = random.randint(2, 5)
        problems[x] = int(int1 / int2)
        print(str(int1) + " / " + str(int2))
    
    given_answers = [0] * len(problems)
    for x in range(0, int(num_of_problems)):
        answer = input("Question " + str(x + 1) + ": ")
        given_answers[x] = answer
    endtime = time.time()
    if num_of_problems > len(given_answers):
        for x in range(0, num_of_problems - len(given_answers)):
            given_answers.append(0)
            
    correctanswers = 0
    
    time.sleep(1)
    check_answers(num_of_problems, given_answers, problems, starttime, endtime)
    
def handle_addition():
    
    print("Welcome to Addicting Addition!")
    
    problems = handle_difficulty()
    num_of_problems = len(problems)
    time.sleep(2)
    
    os.system("printf '\033c'")
    instructions()
    
    starttime = time.time()
    for x in range(0, int(num_of_problems)):
        int1 = random.randint(1, 50)
        int2 = random.randint(1, 50)
        problems[x] = int1 + int2
        print(str(int1) + " + " + str(int2))
    
    given_answers = [0] * len(problems)
    for x in range(0, int(num_of_problems)):
        answer = input("Question " + str(x + 1) + ": ")
        given_answers[x] = answer
    endtime = time.time()
    if num_of_problems > len(given_answers):
        for x in range(0, num_of_problems - len(given_answers)):
            given_answers.append(0)
            
    correctanswers = 0
    
    time.sleep(1)
    check_answers(num_of_problems, given_answers, problems, starttime, endtime)
    
def handle_subtraction():
    
    print("Welcome to Super Subtracting!")
    
    problems = handle_difficulty()
    num_of_problems = len(problems)
    time.sleep(2)
    
    os.system("printf '\033c'")
    instructions()
    
    starttime = time.time()
    for x in range(0, int(num_of_problems)):
        int1 = random.randint(1, 50)
        int2 = random.randint(1, 50)
        problems[x] = int1 - int2
        print(str(int1) + " - " + str(int2))
    
    given_answers = [0] * len(problems)
    for x in range(0, int(num_of_problems)):
        answer = input("Question " + str(x + 1) + ": ")
        given_answers[x] = answer
    endtime = time.time()
    if num_of_problems > len(given_answers):
        for x in range(0, num_of_problems - len(given_answers)):
            given_answers.append(0)
            
    correctanswers = 0
    
    time.sleep(1)
    check_answers(num_of_problems, given_answers, problems, starttime, endtime)

def handle_random():
    
    print("Welcome to Math Madness!")
    
    problems = handle_difficulty()
    num_of_problems = len(problems)
    time.sleep(2)
    
    os.system("printf '\033c'")
    instructions()
    
    starttime = time.time()
    for x in range(0, int(num_of_problems)):
        int1 = random.randint(1, 50)
        int2 = random.randint(1, 50)
        int3 = random.randint(1, 10)
        int4 = random.randint(1, 10)
        int5 = random.randint(1, 4)
        if int5 == 1:
            problems[x] = int1 - int2
            print(str(int1) + " - " + str(int2))
        if int5 == 2:
            problems[x] = int1 + int2
            print(str(int1) + " + " + str(int2))
        if int5 == 3:
            problems[x] = int3 * int4
            print(str(int3) + " * " + str(int4))
        if int5 == 4:
            mod = False
            while mod == False:
                if int1 % int5 == 0:
                    mod = True
                else:
                    int1 = random.randint(1, 50)
                    int5 = random.randint(1, 4)
            problems[x] = int(int1 / int5)
            print(str(int1) + " / " + str(int5))
    
    given_answers = [0] * len(problems)
    for x in range(0, int(num_of_problems)):
        answer = input("Question " + str(x + 1) + ": ")
        given_answers[x] = answer
    endtime = time.time()
    if num_of_problems > len(given_answers):
        for x in range(0, num_of_problems - len(given_answers)):
            given_answers.append(0)
            
    correctanswers = 0
    
    time.sleep(1)
    check_answers(num_of_problems, given_answers, problems, starttime, endtime)
    
def handle_choice(choice):
    if choice == MULTIPLICATION_CHOICE:
        os.system('clear')
        handle_multiplication()
    elif choice == DIVISION_CHOICE:
        os.system('clear')
        handle_division()
    elif choice == ADDITION_CHOICE:
        os.system('clear')
        handle_addition()
    elif choice == SUBTRACTION_CHOICE:
        os.system('clear')
        handle_subtraction()
    elif choice == RANDOM_CHOICE:
        os.system('clear')
        handle_random()
    elif choice == QUIT_CHOICE:
        os.system('clear')
        print("\nExiting the program...\n")
        time.sleep(2)
        print("Thank you!")
        time.sleep(2)
    else:
        print("Error: Invalid selection.")

def display_menu():
    print("\nMENU\n")
    print("1) Multiplication Game")
    print("2) Division Game")
    print("3) Addition Game")
    print("4) Subtraction Game")
    print("5) Any Operation Game")
    print("6) Quit\n")
    
main()