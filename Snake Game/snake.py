import turtle as t

class Snake:
    def __init__(self):
        self.snake_body = []
        for i in range(3):
            self.snake_body.append(t.Turtle())
            self.snake_body[i].penup()
            self.snake_body[i].goto(-(i*20), 0)
            self.snake_body[i].shape("square")  
            self.snake_body[i].color("white") 
    def move(self):
        for i in range(1, len(self.snake_body), 1):
            new_x = self.snake_body[i-1].xcor()
            new_y = self.snake_body[i-1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.snake_body[0].forward(20)
        
    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)
    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)
    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)
    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)
