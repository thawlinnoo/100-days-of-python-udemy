# bug is key, an error in a program..... is value
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
# }


# print(programming_dictionary["Function"])

# add new key in dictionary
# programming_dictionary["Logic"] = "new key"

# print(programming_dictionary)

#wipe out the whole dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#edit the value of the key in dictionary
# programming_dictionary["Bug"] = "edited value"
# print(programming_dictionary)

# Loop in dictionary, only give key.. not value
# for i in programming_dictionary:
#     print(i)

#nested list in dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

#Nested Lists
# nested_list = ["A", "B", ["C", "D"]]

# Nesting a Dictionary inside a Dictionary
# travel_log = {
#   "France": {
#     "cities_visited": ["Paris", "Lille", "Dijon"], 
#     "total_visits": 12
#    },
#   "Germany": {
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#     "total_visits": 5
#    },
# }

# final project
import art

memory = {}
print(art.logo2)
wanna_continue = True
while wanna_continue:
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))
    memory[name] = bid
    user_choice = input("Are there any other bidders? 'yes' or 'no': ").lower()
    if user_choice == "no":
        highest = None
        for i in memory:
            if memory[i] > highest:
                winner = i
                highest = memory[i]
                              
        print(f"{winner} won the bid with {highest}")
        wanna_continue = False
    
#  i can use this to find the max as well
# highest = max(memory, key=memory.get)
