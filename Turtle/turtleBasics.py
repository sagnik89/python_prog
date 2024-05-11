from turtle import *
import random
import heroes

timmy = Turtle()
# timmy.width(4)
timmy.speed("fastest")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "cyan", "magenta", "purple"]

def square():
    for i in range(0, 4):
        timmy.forward(100)
        timmy.right(90)
# square()

def dashed_line():
    for i in range(0, 50):
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()

# dashed_line()

def different_sides():
    t = 0
    for i in range(3, 11):
        angle = 360/i
        for j in range(i):
            timmy.forward(100)    
            timmy.left(angle)
        timmy.color(colors[t])
        t += 1
# different_sides()

directions = [0, 90, 180, 270]

def random_walk():
    repetitions = 200
    for i in range(repetitions):
        direction_choice = random.choice(directions)
        timmy.setheading(direction_choice)
        timmy.forward(20)
        timmy.color(random.choice(colors))
# random_walk()

def spirograph(radius, total_circles):
    # total_circles should be less than 360
    angle = int(360/total_circles)
    for i in range(0, 360, angle):
        timmy.color(random.choice(colors))
        timmy.setheading(i)
        timmy.circle(radius)
    
# spirograph(100, 60)



    


screen = Screen()
screen.exitonclick()

# print(heroes.gen())
