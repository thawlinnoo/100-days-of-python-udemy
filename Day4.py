# print random integer between a and b (a <= n <= b)
# import random
# random_number = random.randint(1,10)
# print(random_number)

# print random float between 0 and 1 (a <= n < b)
# multiply by 10 to get between 0 and 10
# import random
# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# print random float between 0 and 1 (a <= n <= b)
# import random
# random_number_0_to_10 = random.uniform(0,10)
# print(random_number_0_to_10)

# Print Head or Tail randomly
# import random
# result = random.randint(0,1)
# if result == 0:
#     print("Head")
# else:
#     print("Tail")

# Picking random people
# option 1
# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# result = random.randint(0,len(friends)-1)
# print(friends[result])
# option 2
# print(random.choice(friends))

#final project
import random
options = ["Rock", "Paper", "Scissors"]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.: "))
computer_choice = random.randint(0,2)
print(f"User choice is {options[user_choice]}")
print(f"Computer choice is {options[computer_choice]}")
if computer_choice == user_choice:
    print("Draw")
else :
    if computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice == 2 and user_choice == 0:
        print("You Win")
    else:
        if computer_choice > user_choice:
            print("You lose")
        else:
            print("You win")
