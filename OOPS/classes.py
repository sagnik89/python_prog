# from turtle import *

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(200)
# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

# print(timmy)

# This is the module to print a table in the terminal
from prettytable import *

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]

table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)

print(table)