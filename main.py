import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
naming_turtle = turtle.Turtle()
naming_turtle.penup()
naming_turtle.hideturtle()

is_game_on = True
data = pandas.read_csv("50_states.csv")
guess = 0

all_states = data.state.to_list()
guessed_states = []

while is_game_on:
    answer_state = screen.textinput(title=f"{guess}/50 States correct", prompt="What's another state's name? ").title()
    # answer_state = "texas"
    # print(answer_state.title())

    if answer_state == "Exit":
        break
    if answer_state.title() in data.values:
        guessed_states.append(answer_state)
        state_row = data[data.state == answer_state.title()]
        x_loc = int(state_row.x)
        y_loc = int(state_row.y)

        naming_turtle.goto(x_loc, y_loc)
        naming_turtle.write(f"{answer_state.title()}")
        # naming_turtle.write(state_row.state.item())    # Pulling neat data from a series
        guess += 1
        if guess == 50:
            is_game_on = False

# states to learn csv

for state in guessed_states:
    all_states.remove(state)

data_dict = { "States to Learn": all_states}
df = pandas.DataFrame(data_dict)
df.to_csv("states_to_learn.csv")
screen.exitonclick()
