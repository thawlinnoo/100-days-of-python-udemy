

# try: #try this first
#     file = open("a_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
# except FileNotFoundError: #if try fail(only with the filenotfounderror).. do this
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else: #it will come if try succeed
#     content = file.read()
#     print(content)
# finally: #will do whatever try is succeed or not
#     file.close()
#     print("File was closed")

#--------------------------------------

# height = float(input("Height: "))
# weight = float(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.") #raise will show the error in terminal

# bmi = weight/height ** 2
# print(bmi)

#--------------------------------------


# fruits = ["Apple", "Pear", "Orange"]

# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print("Fruit pie")

# make_pie(4)

#--------------------------------------

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]


# def count_likes(posts):



#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes = total_likes + post['Likes']
            
#         except KeyError:
#             continue

#     return total_likes
        

# print(count_likes(facebook_posts))
