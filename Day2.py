# Subscription
# print("Hello"[0])

#final project
print("Welcome to the tip calculator")
total_without_tip = float(input("what was the total bill?: "))
tip = float(input("how much tip would you like to give? 10, 12, or 15?: "))
split = int(input("How many people to split the bill?: "))
total_for_each_person = float(total_without_tip+(total_without_tip*(tip/100)))/split
print(f"Each person should pay: {round(total_for_each_person,2)}")
