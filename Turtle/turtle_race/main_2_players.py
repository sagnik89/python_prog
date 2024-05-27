import turtle as t
import random

#writing the text
turtle = t.Turtle()

turtle.penup()
turtle.hideturtle()
turtle.goto(-200, 400)

screen = t.Screen()
screen.setup(1000, 1000)
user_1_name = screen.textinput("USER 1: ", "Enter your name: ").lower().capitalize()
user_2_name = screen.textinput("USER 2: ", "Enter your name: ").lower().capitalize()
user_1_input = screen.textinput(f"{user_1_name}: ", "Enter any color of the rainbow: ").lower().capitalize()
user_2_input = screen.textinput(f"{user_2_name}", "Enter any color of the rainbow: ").lower().capitalize()
bet = screen.textinput("Enter the bet: ", "Amount")
turtles = []

rainbow_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]


turtle.write("The Race is about to start", font=("Verdana", 20, "normal"))
turtle.goto(-200, 400)


line_creator = t.Turtle();

def create_end_line():
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
    
turtle_ranks = []

should_continue = True
while should_continue:
    for i in range(7):
        turtles[i].forward(random.randint(3,13))
        if(turtles[i].xcor() > 290):
            turtle_ranks.append(turtles[i].pencolor())
            turtles[i].hideturtle()
            turtles[i].goto(0,0)
        if len(turtle_ranks) == 7:
            should_continue = False

turtle.clear()
line_creator.clear()
turtle.write(f'Here are the standings: ', font=("Verdana", 20, "normal"))
turtle.goto(-300, 200)
for i in range(len(turtle_ranks)):
    turtle.goto(-300, turtle.ycor() - 50)
    turtle.write(f'{i+1}: {turtle_ranks[i]}', font=("Verdana", 15, "normal"))
    
turtle.goto(-300, -300)
if turtle_ranks.index(user_1_input) < turtle_ranks.index(user_2_input):
    turtle.write(f'{user_1_name} has won the bet of {bet} rupees', font=("Verdana", 15, "normal"))
else:
    turtle.write(f'{user_2_name} has won the bet of {bet} rupees', font=("Verdana", 15, "normal"))


screen.exitonclick()

