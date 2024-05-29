
# TODO open the background image and make the names appear on the names if the correct state name is applied in the text box



import turtle as t
import pandas

def is_string_in_list(search_string, string_list):
    """
    Checks if a search string is present in any of the strings in the list.
    
    Parameters:
    search_string (str): The string to search for.
    string_list (list): The list of strings to search within.
    
    Returns:
    bool: True if the search string is present in any string in the list, False otherwise.
    """
    # Check for presence of the search string in any of the strings in the list
    for s in string_list:
        if search_string in s:
            return True
    return False




screen = t.Screen()
screen.addshape("blank_states_img.gif")

turtle_ob = t.Turtle()
turtle_ob.shape("blank_states_img.gif")

writer = t.Turtle()
writer.hideturtle()
writer.penup()

data_file = pandas.read_csv("50_states.csv")

state_name_list = data_file.state.to_list()

# Create a csv file for all the missed states  

guessed_states = []
missed_states = []


score = 0
incorrect = 0
attempts = 0
while (attempts < 70 and score <= 50):

    attempts = score + incorrect
    user_input = t.textinput(f"{score}/50 inc: {incorrect} attempts: {score + incorrect}", "Enter Name: ").capitalize()


    # To quit the game when needed
    if user_input == "F":
        break

    # Finding the x cor by the name of the state
    # x_cor = data_file[data_file.state == names].x.to_list()[0]

    # Finding the y cor by the name of the state
    # y_cor = data_file[data_file.state == names].y.to_list()[0]

    if is_string_in_list(user_input, state_name_list):
        x_cor = data_file[data_file.state == user_input].x.to_list()[0]
        y_cor = data_file[data_file.state == user_input].y.to_list()[0]
        guessed_states.append(user_input)
        score += 1

        writer.goto(x_cor, y_cor)
        writer.write(user_input, font=("Verdana",5, "normal"))
    else:
        incorrect += 1

for names in state_name_list:
    if not is_string_in_list(names, guessed_states):
        missed_states.append(names)

print(missed_states)



screen.exitonclick()
