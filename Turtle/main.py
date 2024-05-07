from turtle import *
import heroes

timmy = Turtle()

# def square():
#     for i in range(0, 4):
#         timmy.forward(100)
#         timmy.right(90)

# square()
    
# print(heroes.gen())

def dashed_line():
    for i in range(0, 50):
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()

dashed_line()


screen = Screen()
screen.exitonclick()

