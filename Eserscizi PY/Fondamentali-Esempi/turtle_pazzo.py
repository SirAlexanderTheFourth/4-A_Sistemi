import random
import turtle
finesta = turtle.screensize(100, 100, "black")

def main():
    DIR_DIZ={0:0, 1:180, 2:90, 3:-90}
    
    rumba=turtle.Turtle()
    rumba.color("blue")
    rumba.speed(0)
    random.seed(18)
    for i in range(0, 9999):
        direzione=random.randint(0,3)
        rumba.right(DIR_DIZ[direzione])
        rumba.forward(10)

    turtle.done()


if __name__ == "__main__":
    main()