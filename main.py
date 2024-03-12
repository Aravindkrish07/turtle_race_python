import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.forward(15)


def move_bacward():
    tim.backward(15)


def counter_cloclwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_bacward,"s")
screen.onkey(counter_cloclwise,"a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
