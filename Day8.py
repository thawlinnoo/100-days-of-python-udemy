# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
# def greet():
#     print("hello")
#     print("hi")
#     print("hello_hi")
# greet()

# function that allow input
# name = parameter, Thaw = argument
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"Hi {name}")
# greet_with_name("Thaw")

# more than one parameters (positional argument)
# def greet_with_name(name, age):
#     print(f"Hello {name}")
#     print(f"You are {age}")
# greet_with_name("Thaw", 20)

# more than one parameters (keywords argument)
# def greet_with_name(name, age):
#     print(f"Hello {name}")
#     print(f"You are {age}")
# greet_with_name(age = 20, name = "thaw")

# final project
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):
    result = ""
    if direction == "encode":           
            for i in text:
                if i not in alphabet:
                      result += i
                else:
                    current_index = alphabet.index(i) #i get the current index number here
                    result += alphabet[(current_index+shift)%26]
            print(f"Your encrypted message is {result}")
    elif direction == "decode":           
            for i in text:
                if i not in alphabet:
                      result += i
                else:
                    current_index = alphabet.index(i) #i get the current index number here
                    result += alphabet[(current_index-shift)%26]
            print(f"Your decrypted message is {result}")
         

wanna_continue = True
while wanna_continue: 
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    original_text = input("Type your message: ").lower()
    shift_quantity = int(input("Type the shift number: "))
    caesar(direction, original_text, shift_quantity)
    user_choice = input(f"Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()
    if user_choice == "no":
         wanna_continue = False









