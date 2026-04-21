# data_list = []

# with open ("Day-25/weather_data.csv", mode="r") as file:
#     data = file.readlines()

# for days in data:
#     data_list.append(days.strip())

# print(data_list)

# ------------------------------

# import csv

# with open("Day-25/weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# ------------------------------

# import pandas

# data = pandas.read_csv("Day-25/weather_data.csv")
# print(data["temp"]) #better appeal than using csv normally

# print(type(data["temp"])) #one dimension is series, 2 dimensions is data_frame

# data_dict = data.to_dict()
# print(data_dict) #show as dictionary

# data_list = data["temp"].to_list()
# print(data_list) #show as list

# data_list = data["temp"].to_list()
# avg_temp = data["temp"].mean()
# print(round(avg_temp, 2))

# max_temp =  data["temp"].max()
# print(max_temp)

# print(data[data["day"]=="Monday"]) #printing specific row

# max_temp_row = data.loc[data["temp"]==data["temp"].max()]
# max_temp_row["temp"] = (max_temp_row["temp"] * 2) +32
# print(max_temp_row)

# Monday = data[data["day"]== "Monday"]
# print(Monday)
# print(Monday["temp"])

#Create dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]

# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("Day-25/new_csv_file")




import pandas
data = pandas.read_csv("Day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260421.csv")
num_of_black = (data["Primary Fur Color"] == "Black").sum()
num_of_gray = (data["Primary Fur Color"] == "Gray").sum()
num_of_cinnamon = (data["Primary Fur Color"] == "Cinnamon").sum()
my_dict = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [num_of_black, num_of_gray, num_of_cinnamon]
}

data = pandas.DataFrame(my_dict)
data.to_csv("Day-25/squirrel_count.csv")













