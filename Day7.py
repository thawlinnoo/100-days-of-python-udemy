# word_list = ["apple", "orange", "mango"]

# import random
# choose random word from the list and print it
# chose_word = word_list[random.randint(0,len(word_list)-1)]
# print(chose_word)
# blanks = ""
# for i in range(0,len(chose_word)):
#     blanks += "_"
# print(blanks)

#ask user to guess the letter
# guess_letter = input("Guess the letter: ").lower()

#check if the user guess is right or wrong
# blanks = ""
# for i in range(0,len(chose_word)):
#     if chose_word[i] == guess_letter:
#         blanks += guess_letter
#     else :
#         blanks += "_"
# print(blanks)


# Step 3
# word_list = ["apple", "orange", "mango"]

# import random

# chose_word = word_list[random.randint(0,len(word_list)-1)]
# print(chose_word)
# blanks = ""
# for i in range(0,len(chose_word)):
#     blanks += "_"
# print(blanks)

# game_over = False
# blanks_list = ["_"]*len(chose_word)
# while not game_over:
#     guess_letter = input("Guess the letter: ").lower()

    
#     for i in range(0,len(chose_word)):
#         if chose_word[i] == guess_letter:
#             blanks_list[i] = guess_letter

#     blanks = ""
#     for i in blanks_list:      
#         blanks += i
    
#     if "_" not in blanks:
#         game_over = True
    
#     print(blanks)

#  Step 4
# stages = [
#     """
#      -----
#      |   |
#          |
#          |
#          |
#          |
#     =========
#     """,
#     """
#      -----
#      |   |
#      O   |
#          |
#          |
#          |
#     =========
#     """,
#     """
#      -----
#      |   |
#      O   |
#      |   |
#          |
#          |
#     =========
#     """,
#     """
#      -----
#      |   |
#      O   |
#     /|   |
#          |
#          |
#     =========
#     """,
#     """
#      -----
#      |   |
#      O   |
#     /|\  |
#          |
#          |
#     =========
#     """,
#     """
#      -----
#      |   |
#      O   |
#     /|\  |
#     /    |
#          |
#     =========
#     """,
#     """
#      -----
#      |   |
#      O   |
#     /|\  |
#     / \  |
#          |
#     =========
#     """
# ]

# word_list = ["apple", "orange", "mango"]

# import random

# chose_word = word_list[random.randint(0,len(word_list)-1)]
# print(chose_word)
# blanks = ""
# for i in range(0,len(chose_word)):
#     blanks += "_"
# print(blanks)

# lives = 0
# game_over = False
# blanks_list = ["_"]*len(chose_word)
# while not game_over:
#     guess_letter = input("Guess the letter: ").lower()

#     if guess_letter not in chose_word:
#         lives += 1
#         print(stages[lives])
#     else:
#         for i in range(0,len(chose_word)):
#             if chose_word[i] == guess_letter:
#                 blanks_list[i] = guess_letter
            
#         blanks = ""
#         print(stages[lives]) 
#         for i in blanks_list:      
#             blanks += i
    
#     if "_" not in blanks:
#             game_over = True
#             print ("You won")
#     elif lives == 6:
#         game_over = True
#         print ("You lose")
          
#     print(blanks)


# Step 5
stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """
]



import random
import hangman_word_list

chose_word = hangman_word_list.word_list[random.randint(0,len(hangman_word_list.word_list)-1)]
print(chose_word)
blanks = ""
for i in range(0,len(chose_word)):
    blanks += "_"
print(blanks)

lives = 0
remaining_lives = 6
game_over = False
blanks_list = ["_"]*len(chose_word)
wrong_guess = ""

while not game_over:
    guess_letter = input("Guess the letter: ").lower()
    
    

    if guess_letter not in chose_word and guess_letter not in wrong_guess:
        wrong_guess += guess_letter
        lives += 1
        remaining_lives -= 1
        print(f"you guess {guess_letter}. It is not in the chosen word. You lost one life")
        print(stages[lives])
    elif guess_letter in wrong_guess:
        print("You already make that wrong guess")
        print(stages[lives])
    else:
        for i in range(0,len(chose_word)):
            if chose_word[i] == guess_letter:
                blanks_list[i] = guess_letter
            
        blanks = ""
        print(stages[lives]) 
        for i in blanks_list:      
            blanks += i
    
    print(f"You have {remaining_lives} left.")
    if "_" not in blanks:
            game_over = True
            print ("You won")
    elif lives == 6:
        game_over = True
        print ("You lose")
    
          
    print(blanks)