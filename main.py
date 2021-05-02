import turtle
import pandas

screen = turtle.Screen()
screen.title("United States Game")
image = "blank_states_img.gif" # path to reach image(blank_states_img.gif)
screen.addshape(image) # load this image to screen
turtle.shape(image) # change turtle's shape to image's shape

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() # in list form
guessed_states = []


while len(guessed_states) < 50:
    # 1 convert the guess to Title case: title make first letter capitalized
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # save missing states in csv file:
        # missing_state = []
        # for states in all_states:
        #     if states not in guessed_states:
        #         missing_state.append(states)
        missing_state = [state for state in all_states if state not in guessed_states] # list comprehension
        # print(missing_state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn")
        break # end while loop

    # if they got it right:
    if answer_state in all_states: # if answer_state is one of the states in all the states of the 50_states.csv
        guessed_states.append(answer_state)
        # create a turtle to write the name of the state at the state's x & y coordinate
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] # get row where state is equal to answer to state
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state) # state_data.state is equal to answer_state, and no junk information
        # t.write(answer_state.state.item()), item() is method of pandas series, return first element of data

#2 check if the guess is among the 50 states
#3 write correct guesses onto map
#4 use a loop to allow the user to keep guessing
#5 record the correct guess in a list
#6 keep track of the score

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop() # alternative way of keeping our screen open even though our code has finished running, same as screen.exitonclick()
# screen.exitonclick() # but we don't want to exit when clicking, so we use turtle.mainloop this time.