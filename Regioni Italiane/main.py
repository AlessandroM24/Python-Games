import turtle
import pandas

screen = turtle.Screen()
screen.title("Stati Italiani")
image = "regioni_italia.gif"
screen.bgpic(image)

data = pandas.read_csv("regioni.csv")
states_list = data.state.to_list()
guessed_states = []

x_list = data.x
y_list = data.y

for state in states_list:
    x = x_list[states_list.index(state)]
    y = y_list[states_list.index(state)]

score = 0

while score < 20:
    answer_state = screen.textinput(title=f"{score} / 20 Regioni Corrette",
                                    prompt="Scrivi un'altra regione").title()
    if answer_state in states_list and answer_state not in guessed_states:
        score += 1
        guessed_states.append(answer_state)

        x = x_list[states_list.index(answer_state)]
        y = y_list[states_list.index(answer_state)]

        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x, y)
        turtle.penup()
        turtle.write(answer_state, font=("Arial", 8, "normal"))

turtle.mainloop()  # Schermo sempre aperto.
