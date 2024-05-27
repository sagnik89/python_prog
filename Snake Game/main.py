import turtle as t 
import time
import snake
import food

screen = t.Screen()
screen.listen()

screen.setup(height=600, width= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

my_snake = snake.Snake()  
my_food = food.Food()

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()

    # Detecting the collision between the food and the snake
    if my_snake.snake_body[0].distance(my_food) < 15:
        my_food.refresh()



    screen.onkeypress(my_snake.up, "Up")
    screen.onkeypress(my_snake.down, "Down")
    screen.onkeypress(my_snake.left, "Left")
    screen.onkeypress(my_snake.right, "Right")


screen.exitonclick()
