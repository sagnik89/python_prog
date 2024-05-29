import pandas

data = pandas.read_csv("squirrel_data.csv")

fur_color = data["Primary Fur Color"]    

fur_color_list = fur_color.to_list()

print(fur_color_list )

gray_count = 0
cinnamon_count = 0
black_count = 0


for item in fur_color_list:
    if item == "Gray":
        gray_count += 1
    
    if item == "Black":
        black_count += 1
    
    if item == "Cinnamon":
        cinnamon_count += 1


dict ={
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Color Count": [gray_count, black_count, cinnamon_count]
}

new_data_file = pandas.DataFrame(dict)

new_data_file.to_csv("new_file")

    

