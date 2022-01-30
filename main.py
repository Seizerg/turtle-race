from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "green", "yellow", "purple", "blue", "orange"]
turtles = []
isOn = False


def create_turtles():
    y_cord = -100
    for i in range(len(colors)):
        turtles.append(Turtle(shape="turtle"))
        turtles[i].penup()
        turtles[i].color(colors[i])
        turtles[i].goto(x=-230, y=y_cord)
        y_cord += 40


choice = screen.textinput(title="Make a bet!!", prompt="Choose a turtle you wanna bet on")
create_turtles()
if choice:
    isOn = True

while isOn:
    for turtle in turtles:
        if turtle.xcor() > 225:
            if turtle.pencolor() == choice:
                print("You win!!")
            else:
                print("You lost")
            print(f"Race is won by {turtle.pencolor()} turtle")
            isOn = False
        turtle.fd(random.randint(0, 10))

screen.exitonclick()
