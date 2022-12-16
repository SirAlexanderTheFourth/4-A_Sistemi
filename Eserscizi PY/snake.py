import turtle 

finesta = turtle.screensize(100, 100, "black")
rumba=turtle.Turtle()
rumba.color("blue")
clean=turtle.Turtle()
clean.color("black")

def right():
    rumba.setheading(0)

    

def up():
    rumba.setheading(90)

def down():
    rumba.setheading(270)

def left():
    rumba.setheading(180)

def main():
    turtle.onkey(right, 'Right')
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(left, 'Left')
    
    while True:
        rumba.forward(1)
        turtle.listen()
    
    turtle.done()

if __name__ == "__main__":
    main()

