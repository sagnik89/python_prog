import turtle as t
import random

#writing the text
turtle = t.Turtle()
turtle.penup()
turtle.hideturtle()
turtle.goto(-200, 400)

screen = t.Screen()
screen.setup(1000, 1000)
user_input = screen.textinput("Choose your turtle!", "Enter any color of the rainbow: ").lower()
turtles = []

rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]


turtle.write("The Race is about to start", font=("Verdana", 20, "normal"))
turtle.goto(-200, 400)



def create_end_line():
    line_creator = t.Turtle();
    line_creator.penup()
    line_creator.hideturtle()
    line_creator.setx(300)
    line_creator.sety(-200)
    line_creator.setheading(90)
    line_creator.pendown()
    line_creator.forward(500)

create_end_line()


for i in range(7):
    turtles.append(t.Turtle())
    turtles[i].penup()
    turtles[i].shape("turtle")
    turtles[i].color(rainbow_colors[i])
    turtles[i].setx(-400)
    turtles[i].sety(-100 + (i*50))

turtle.clear()
turtle.write("The Race has begun !", font=("Verdana", 20, "normal"))
turtle.goto(-300, 400)
    
should_continue = True
while should_continue:
    for i in range(7):
        turtles[i].forward(random.randint(0,10))
        if(turtles[i].xcor() > 290):
            winning_color = turtles[i].pencolor()
            should_continue = False
            break;

turtle.clear()
if user_input == winning_color:
    output = f'You have won the bet. {winning_color} has won the race'
    turtle.write(output, font=("Verdana", 20, "normal"))
else:
    output = f'You have lost the bet. {winning_color} has won the race\n                      Pay 50 rupees '
    turtle.write(output, font=("Verdana", 20, "normal"))







screen.exitonclick()