# Create a function called format_name() that takes two inputs: f_name and `l_name'.
# Use the title() function to modify the f_name and l_name parameters into Title Case.
# def name_function(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return (f"formatted name is {formatted_f_name} {formatted_l_name}")

# result = name_function(f_name="thaw linn", l_name="oo")
# print (result)

# using another output as the input
# def function_1(text):
#     return text + text

# def function_2(text):
#     return text.title()

# output = function_2(function_1("hello"))
# print(output)

# final project 

import art

def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2

start_new = True
while start_new:
    print(art.logo3)
    continue_old = True
    first_number = float(input("what is the first number?: "))
    while continue_old:
        operator = input("Enter the operator\n+\n-\n×\n÷\n ")
        second_number = float(input("what is the second number?: "))
        if operator == "+":
            result = add(num1=first_number, num2=second_number)
        elif operator == "-":
            result = subtract(num1=first_number, num2=second_number)    
        elif operator == "*":
            result = multiply(num1=first_number, num2=second_number)
        elif operator == "/":
            result = divide(num1=first_number, num2=second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        choice = input(f"Type y to start new or type n to continue by using the {result}: ")
        if choice == "y":
            continue_old = False
        else:
            continue_old = True
            first_number = result
        



