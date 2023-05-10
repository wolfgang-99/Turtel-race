from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet",prompt="which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_range in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_range])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_range])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            wining_color = turtle.pencolor()
            is_race_on = False
            if user_bet == wining_color:
                print(f"you have won! The {wining_color} turtle is the winner")
            else:
                print(f"you have loss! The {wining_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()