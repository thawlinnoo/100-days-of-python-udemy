# finding highest
# score = [23,4,354,6,7,48,54,6,3,2,4,2,342,52]
# highest = score[0]
# for i in score:
#     if i>highest:
#         highest=i
# print(highest)

# add 1 to 100
# result = 0
# for i in range (1,101):
#     result += i
# print(result)



# Final project

import random

letters = [
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
symbols = ['!','#','$','%','&','(',')','*','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']


print("Welcome to the PyPassword Generator!")
require_letters = int(input("How many letters do you like in your password?\n"))
require_symbols = int(input("How many symbols do you like in your password?\n"))
require_numbers = int(input("How many numbers do you like in your password?\n"))


password_list = []
for x in range(0,require_letters):
    password_list.append(letters[random.randint(0,25)])

for x in range(0,require_symbols):
    password_list.append(symbols[random.randint(0,8)])

for x in range(0,require_numbers):
    password_list.append(numbers[random.randint(0,9)])

print(password_list)

for i in range(0,len(password_list)):
    random_index = random.randint(0,len(password_list)-1)
    password_list[i], password_list[random_index] =password_list[random_index], password_list[i]

result = ""
for i in password_list:
    result += i

print(f"Your Password is {result}")



# result = ""
# combine = chose_letters+chose_symbols+chose_numbers
# for x in range(0,len(combine)):
#     if x<len(chose_letters):
#         result+=chose_letters[x]
#         if x<len(chose_symbols):
#             result+=chose_symbols[x]
#             if x<len(chose_numbers):
#                 result+=chose_numbers[x]

# print(result)

