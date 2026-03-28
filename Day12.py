#Local scope - variable declare in a function and cannot access from outside the function
#Global scope - variable declare outside a function and it is accessible anywhere in the code file but cannot modify.
# enemies = 1 #global scope

# def increase_enemies():
#     enemies = 2 #local scope
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Namespaces
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(potion_strength)
    
#     drink_potion()
# game()

#modify global scope
# enemies = 1

# def increase_enemies():
#     # global enemies #we need to declare this to modify global scope
#     enemies += 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#another way to modify global scope
# enemies = 1

# def increase_enemies(enemy):

#     print(f"enemies inside function: {enemies}")
#     return enemy + 1

# enemies = increase_enemies(enemies)
# print(f"enemies outside function: {enemies}")

#final project
import random
answer = random.randint(1,100)
level = input("choose the mode. easy mode for 10 lives and hard mode for 5 lives: easy or hard: ")
if level=="easy":
    life = 10
else:
    life = 5
while life > 0:
    user_choice = int(input("Choose the number from 1 to 100:"))
    if user_choice>answer:
        life -= 1
        print("The guess is too high.")
        print(f"You've got {life} life remaining")
        
    elif user_choice<answer:
        life -= 1
        print("The guess is too low.")
        print(f"You've got {life} life remaining")
    else:
        print("You won")
        break

if life==0:
    print("you run out of lives... You lose")
    print(f"The answer is {answer}")

#final project using functions
import random
answer = random.randint(1,100)

def game():
    def set_difficulty():
        level = input("choose the mode. easy mode for 10 lives and hard mode for 5 lives: easy or hard: ")
        if level=="easy":
            life = 10
            return life
        else:
            life = 5
            return life


    def check_guess():
        life = set_difficulty()
        while life > 0:
            user_choice = int(input("Choose the number from 1 to 100:"))
            if user_choice>answer:
                life -= 1
                print("The guess is too high.")
                print(f"You've got {life} life remaining")
                
            elif user_choice<answer:
                life -= 1
                print("The guess is too low.")
                print(f"You've got {life} life remaining")
            else:
                print("You won")
                break

        if life==0:
            print("you run out of lives... You lose")
            print(f"The answer is {answer}")
    
    check_guess()

game()

# another version for final project
import random

def set_difficulty():
    level = input("Choose mode: easy or hard: ").lower()
    if level == "easy":
        return 10
    else:
        return 5

def check_guess(answer):
    life = set_difficulty()

    while life > 0:
        user_choice = int(input("Choose the number from 1 to 100: "))

        if user_choice > answer:
            life -= 1
            print("The guess is too high.")
            print(f"You've got {life} lives remaining")

        elif user_choice < answer:
            life -= 1
            print("The guess is too low.")
            print(f"You've got {life} lives remaining")

        else:
            print("You won")
            return

    print("You ran out of lives... You lose")
    print(f"The answer is {answer}")

def game():
    answer = random.randint(1, 100)
    check_guess(answer)

game()
    


#udemy one

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")
        return turns


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print(f"You've run out of guesses, you lose. The answer was {answer}")
            return
        elif guess != answer:
            print("Guess again.")


game()