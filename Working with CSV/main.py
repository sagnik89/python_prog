# importing data like this will take much of an effort to extract the data

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# Rather use csv import but this too becomes complex when bigger projects are introduced
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for rows in data:
#         temp = rows[1]

#         if rows[1] != 'temp':
#             temperatures.append(int(rows[1]))
    
#     print(temperatures)

# That's why we use pandas

# import pandas

# data = pandas.read_csv("weather_data.csv")

# temperatures = data["temp"].to_list()                

# sum = 0
# for num in temperatures:
#     sum = sum + num;

# print(sum/len(temperatures))

# max_temp = data["temp"].max()

# print(data[data["temp"] == max_temp])

# monday_temp = data[data.day == "Monday"].temp

# print(((9 * monday_temp)/5) + 32)

   