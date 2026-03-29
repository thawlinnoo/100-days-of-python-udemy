# import random
# import art
# import game_data

# def choosing_candidate():
#     return(game_data.data[random.randint(0,len(game_data.data)-1)])

# def game():
#     wrong = False
#     score = 0
#     first_candidate = choosing_candidate()
#     second_candidate = choosing_candidate()
#     print(art.logo4)
#     print(f"Compare A: {first_candidate['name']}, {first_candidate['description']}, from {first_candidate['country']}")
#     print("")
#     print(art.vs)
#     print(f"Compare B: {second_candidate['name']}, {second_candidate['description']}, from {second_candidate['country']}")
#     user_choice = input("Who has more follower? Type 'A' or 'B': ").upper()
#     if first_candidate["follower_count"]>second_candidate["follower_count"]:
#         more_follower = "A"
#     else:
#         more_follower = "B"
#     if user_choice!=more_follower:
#         print(f"Wrong, your score is {score}")      
#     else:
#         score += 1
#         print(f"Right, ur current score is {score}")
#         while not wrong:
#             first_can = second_candidate
#             second_can = choosing_candidate()
#             print(art.logo4)
#             print(f"Compare A: {first_can['name']}, {first_can['description']}, from {first_can['country']}")
#             print("")
#             print(art.vs)
#             print(f"Compare B: {second_can['name']}, {second_can['description']}, from {second_can['country']}")
#             user_choice = input("Who has more follower? Type 'A' or 'B': ").upper()
#             if first_can["follower_count"]>second_can["follower_count"]:
#                 more_follower = "A"
#             else:
#                 more_follower = "B"
#             if user_choice!=more_follower:
#                 print(f"Wrong, your score is {score}") 
#                 wrong = True     
#             else:
#                 score += 1
#                 print(f"Right, ur current score is {score}")
                    
# game()



import random
from art import logo4, vs
from game_data import data

def choosing_candidate():
    return(random.choice(data))

def check(user_choice, first_candidate, second_candidate):
    if first_candidate["follower_count"] > second_candidate["follower_count"] and user_choice=="A":
        return True
    elif first_candidate["follower_count"] < second_candidate["follower_count"] and user_choice=="B":
        return True
    else:
        return False


def game():
    wrong = False
    score = 0
    second_candidate = choosing_candidate()
    while not wrong:
        first_candidate = second_candidate
        second_candidate = choosing_candidate()
        while first_candidate == second_candidate:
            second_candidate = choosing_candidate()
        print(logo4)
        print(f"Compare A: {first_candidate['name']}, {first_candidate['description']}, from {first_candidate['country']}")
        print("")
        print(vs)
        print(f"Compare B: {second_candidate['name']}, {second_candidate['description']}, from {second_candidate['country']}")
        user_choice = input("Who has more follower? Type 'A' or 'B': ").upper()
        result = check(user_choice, first_candidate, second_candidate )
        if result:
            score += 1
            print(f"Right, your current score is {score}")
        elif not result:
            print(f"Wrong, your score is {score}")
            wrong = True
game()









