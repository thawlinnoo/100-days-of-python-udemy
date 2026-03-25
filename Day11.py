
import random
import art
print(art.logo4)

wanna_play = True

def compare (user_score, computer_score):
    if user_score> 21 and computer_score>21:
            print("Draw")
    elif user_score>21 and computer_score<=21:
        print("You lose")
    elif user_score<=21 and computer_score>21:
        print("You Win")
    elif user_score == computer_score:
        print("Draw")
    elif user_score > computer_score:
        print("You win")
    elif user_score < computer_score:
        print("Computer win")


while wanna_play:

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_card_list = []
    user_card_list = []

    computer_current_score = 0
    user_current_score = 0

    computer_first_card = cards[random.randint(0, len(cards)-1)]
    computer_card_list.append(computer_first_card)
    computer_current_score+=computer_first_card
    computer_second_card = cards[random.randint(0, len(cards)-1)]
    computer_card_list.append(computer_second_card)
    computer_current_score+=computer_second_card

    while computer_current_score < 17:
        computer_choice = cards[random.randint(0, len(cards)-1)]
        computer_card_list.append(computer_choice)
        computer_current_score+=computer_choice
        for i in range(0,len(computer_card_list)):
            if computer_current_score>21 and computer_card_list[i]==11:
                computer_card_list[i]=1
                computer_current_score-=10

    user_first_card = cards[random.randint(0, len(cards)-1)]
    user_card_list.append(user_first_card)
    user_current_score+=user_first_card
    user_second_card = cards[random.randint(0, len(cards)-1)]
    user_card_list.append(user_second_card)
    user_current_score+=user_second_card

    if user_current_score==21:
        print(f"Your final hand {user_card_list}, current score: {user_current_score}")
        print(f"Computer final hand {computer_card_list}, current score: {computer_current_score}")
        compare(user_score = user_current_score, computer_score = computer_current_score)
        play = input("still wanna play game? y or n?: ")
        if play == "y":
            wanna_play = True
        else:
            wanna_play = False
        continue
        

    print(f"Your card: {user_card_list}, current score {user_current_score}")
    print(f"Computer first card: {computer_card_list[0]}")
    get_another_card = input("Press y to get another card or press n to pass: ")
    if get_another_card == "y":
        chose_to_pass = False
    else:
        chose_to_pass = True
        print(f"Your final hand {user_card_list}, current score: {user_current_score}")
        print(f"Computer final hand {computer_card_list}, current score: {computer_current_score}")
        compare(user_score = user_current_score, computer_score = computer_current_score)
        play = input("still wanna play game? y or n?: ")
        if play == "y":
            wanna_play = True
        else:
            wanna_play = False
        continue
        
        

    while user_current_score<21 and not chose_to_pass:
        user_choice = cards[random.randint(0, len(cards)-1)]
        user_card_list.append(user_choice)
        user_current_score+=user_choice
        for i in range(0, len(user_card_list)):
            if user_current_score>21 and user_card_list[i]==11:
                user_card_list[i]=1
                user_current_score-=10
        if user_current_score>=21:
            print(f"Your final hand {user_card_list}, current score: {user_current_score}")
            print(f"Computer final hand {computer_card_list}, current score: {computer_current_score}")
            compare(user_score = user_current_score, computer_score = computer_current_score)
            play = input("still wanna play game? y or n?: ")
            if play == "y":
                wanna_play = True
            else:
                wanna_play = False
            continue
            

        print(f"Your card: {user_card_list}, current score {user_current_score}")
        print(f"Computer first card: {computer_card_list[0]}")
        get_another_card = input("Press y to get another card or press n to pass: ")
        if get_another_card == "y":
            chose_to_pass = False
        else:
            chose_to_pass = True
            print(f"Your final hand {user_card_list}, current score: {user_current_score}")
            print(f"Computer final hand {computer_card_list}, current score: {computer_current_score}")
            compare(user_score = user_current_score, computer_score = computer_current_score)
            play = input("still wanna play game? y or n?: ")
            if play == "y":
                wanna_play = True
            else:
                wanna_play = False
            continue
            
        

