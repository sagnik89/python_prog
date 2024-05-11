import turtle as t 
screen = t.Screen()



screen.setup(height=600, width= 600)
screen.bgcolor("black")
screen.title("My Snake Game")

turtles = []

for i in range(3):
    turtles.append(t.Turtle())
    turtles[i].penup()
    turtles[i].goto(-(i*20), 0)
    turtles[i].shape("square")
    turtles[i].color("white")






screen.exitonclick()

