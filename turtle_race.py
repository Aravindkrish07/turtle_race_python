from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
colors =["red","blue","green", "yellow", "purple", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []


screen.setup(width=500, height=400)
user_txt = screen.textinput(title="make your bet", prompt="which turtle will win the race? enter the color: ")
print(user_txt)

for i in range(0,5):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtle.append(new_turtle)

if user_txt:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_txt:
                print("you won")
            else:
                print("you lost")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


