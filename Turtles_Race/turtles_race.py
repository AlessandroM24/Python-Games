from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)  # Set the window resolution.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle wii win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # Colors
turtles_list = []
X_FINISH_LINE = 200


def create_turtles():
    y_turtle = -100
    for color in colors:
        turtle_object = Turtle("turtle")
        turtles_list.append(turtle_object)
        turtle_object.penup()
        turtle_object.color(color)
        turtle_object.goto(x=-230, y=y_turtle)
        y_turtle += 50


def move_turtles(turtles):
    no_winner = True

    while no_winner:
        for turtle_object in turtles:
            turtle_object.forward(random.randint(1, 8))

            if turtle_object.xcor() >= X_FINISH_LINE:
                print(f"The {turtle_object.pencolor()} turtle won the race!")
                print(check_bet_win(turtle_object.pencolor(), user_bet))
                no_winner = False


def check_bet_win(turtle_object_color, bet):
    if turtle_object_color.lower() == bet.lower():
        return "Bet: won"
    else:
        return "Bet: lost"


def print_finish_line():
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.pensize(10)
    finish_line.penup()
    finish_line.goto(X_FINISH_LINE, 200)
    finish_line.right(90)
    finish_line.pendown()
    finish_line.forward(400)


def main():
    print_finish_line()
    create_turtles()
    move_turtles(turtles_list)


main()
screen.exitonclick()
