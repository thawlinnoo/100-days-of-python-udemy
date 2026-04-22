# list comprehension 
# add 1 to each int in the list

# numbers = [1,2,3]
# new_numbers = [num + 1 for num in numbers]
# print(new_numbers)

#---------------------------------

# new_numbers = [num * 2 for num in range(1,5)]
# print(new_numbers)


#---------------------------------


# #Conditional List comprehension
# names = ["alex", "beth", "carline", "dave", "elanor", "Freddie"]
# all_cap_list = [name.upper() for name in names if len(name)>5]
# print(all_cap_list)

#---------------------------------

#Dictionary comprehension
# import random
# names = ['Alex', 'Beth', 'Carline', 'Dave', 'Elanor', 'Freddie']
# student_score = {
#     student:random.randint(0,100) for student in names
# }
# print(student_score)
# passed_student = {
#     student:student_score[student] for student in student_score if student_score[student]>50
# }
# print(passed_student)

#---------------------------------

#different version(use item() so python know not only key but also value)
# import random 
# names = ['Alex', 'Beth', 'Carline', 'Dave', 'Elanor', 'Freddie'] 
# student_score = { 
#     student:random.randint(0,100) for student in names 
# } 
# print(student_score) 
# passed_student = { 
#     student:score for (student, score) in student_score.items() if score>50 
# } 
# print(passed_student)

#---------------------------------

#iterate pandas dataframe
import pandas
student_score = {
    "name" : ['Alex', 'Beth', 'Carline', 'Dave', 'Elanor', 'Freddie'],
    "score" : [26, 75, 89, 75, 88, 97]
}
student_score_data_frame = pandas.DataFrame(student_score)
print(student_score_data_frame)

for (index, row) in student_score_data_frame.iterrows():
    print(row["name"])

