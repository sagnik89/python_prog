import turtle as t 
import time
import snake

screen = t.Screen()
screen.listen()

screen.setup(height=600, width= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

my_snake = snake.Snake()   


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    screen.onkeypress(my_snake.up, "Up")
    screen.onkeypress(my_snake.down, "Down")
    screen.onkeypress(my_snake.left, "Left")
    screen.onkeypress(my_snake.right, "Right")


screen.exitonclick()
