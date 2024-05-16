import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
# turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

x_list = data.x
y_list = data.y

for state in states_list:
    x = x_list[states_list.index(state)]
    y = y_list[states_list.index(state)]

score = 0

while score < 50:
    answer_state = screen.textinput(title=f"{score} / 50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state in states_list:
        score += 1

        x = x_list[states_list.index(answer_state)]
        y = y_list[states_list.index(answer_state)]

        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x, y)
        turtle.penup()
        turtle.write(answer_state, font=("Arial", 8, "normal"))

turtle.mainloop()  # Schermo sempre aperto.
