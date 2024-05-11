import turtle as t

timmy = t.Turtle()
timmy.speed("fast")

def move_forward():
    timmy.forward(10)
    
def rotate_right():
    timmy.right(12)    

def rotate_left():
    timmy.left(12)

def move_backwards():
    timmy.backward(10)        

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.sety(0)
    timmy.setx(0)
    timmy.setheading(0)
    timmy.pendown()


t.onkeypress(move_forward, "w")
t.onkeypress(rotate_left, "a")
t.onkeypress(rotate_right, "d")
t.onkeypress(clear_screen, "c")
t.onkeypress(move_backwards, "s")



screen = t.Screen()
screen.listen()
screen.exitonclick()