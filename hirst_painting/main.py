# import colorgram

# colors = colorgram.extract('hirst_painting\image.png', 64)

# color_list = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)

# print(color_list)

import turtle
import random


# Colors extracted by the use of colorgram module
color_list = [(252, 250, 247), (253, 247, 249), (237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155), (238, 157, 212), (86, 77, 208), (86, 225, 235), (250, 8, 14), (242, 166, 157), (177, 180, 224), (36, 243, 159), (6, 81, 115), (11, 55, 248)]

timmy = turtle.Turtle()
turtle.colormode(255)


timmy.penup()
timmy.setx(-200)
timmy.sety(-200)


def go_to_next_row():
    timmy.sety(timmy.ycor() + 10)
    pass
def print_dots_in_line():
    pass

timmy.color("red")
timmy.penup()
timmy.forward(100)
timmy.color("green")
timmy.pendown()



screen = Screen()
screen.exitonclick()



    
