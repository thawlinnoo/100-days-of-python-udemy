#final project
print("Welcome to Treasure Island. Your mission is to find the treasure.")
ans = input("left or right?: ")
if ans == "right":
    print("Game over")
elif ans == "left":
    ans = input("swim or wait?: ")
    if ans == "swim":
        print("Game over")
    elif ans == "wait":
        ans = input("Which door? red or blue or yellow: ")
        if ans == "red":
            print("Game over")
        elif ans == "blue":
            print("Game over")
        elif ans == "yellow":
            print("You win")