

name_list = []
with open("Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()
   

for name in names:
    name_list.append(name.strip())

letter = """Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Thaw"""

for i in range(len(name_list)):
    ready_letter = letter.replace("[name]", name_list[i])
    with open(f"Mail Merge Project Start/Output/ReadyToSend/letter_for_{name_list[i]}", mode = "w") as file:
        file.write(ready_letter)



    


