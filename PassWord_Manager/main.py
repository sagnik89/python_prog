# This is a password manager App. 
# Inputs -> Website, Username, password (can be generated)
# One more option of Adding the files to a .txt file which acts as a database

from tkinter import *
import prettytable as prettyTb
import random
import os 
import subprocess
import platform

table = prettyTb.PrettyTable()

# Colors used 
YELLOW = "#FFE8C8"
WHITE = "#FFFFFF"
FONT_NAME = "Courier"


def open_file_system(filename):
    """
    Opens a file with the default application in the operating system.

    :param filename: The name of the file to open.
    """
    try:
        if platform.system() == 'Windows':
            os.startfile(filename)
        elif platform.system() == 'Darwin':  # macOS
            subprocess.call(['open', filename])
        else:  # Linux and other Unix-like systems
            subprocess.call(['xdg-open', filename])
    except Exception as e:
        print(f"Error: Unable to open the file. Details: {e}")


""" Creating the UI of the Password Manager App """

# Main window
root = Tk()
root.title("Password Manager")
root.maxsize(600, 600)
root.minsize(600, 600)
root.config(bg=WHITE)

# Canvas for the password manager image
canvas = Canvas(width=200, height= 200, bg=YELLOW, highlightthickness=0)
lock_image = PhotoImage(file="lock_image.png")
canvas.create_image(100, 100, image=lock_image)
canvas.place(x=200, y=120)

# Figuring out why the canvas is not centering itself -> Found out reason that because there are no other components

# Creating two input text areas and an output/input text area
# 1 -> Website
# 2 -> Username
# 3 -> Password  

webiste_label = Label(root, text="Website:", bg=WHITE, font=(FONT_NAME))
webiste_label.place(x=110, y=350)

website_name = Entry(root)
website_name.place(x=230, y=345)

user_label = Label(root, text="Username:", bg=WHITE, font=(FONT_NAME))
user_label.place(x=110, y=400)



user_name = Entry(root)
user_name.place(x=230, y=395)

password_label = Label(root, text="Password:", bg=WHITE, font=(FONT_NAME))
password_label.place(x=110, y = 450)


password = Entry(root)

password.place(x=230, y=445)


""" Creating Functions for the buttons """

def add_to_file():
    website = website_name.get()
    user = user_name.get()
    password_name = password.get()

    current_list = [website, user, password_name] 

    table.field_names=["Website", "Username", "Password"]
    table.add_row(current_list)

    data_string = table.get_string()


    with open("data.txt", "w") as file:
        file.write(data_string)        
    
    clear_all()

    
my_password_var = StringVar()

def generate_password():

    my_password = ""

    # To clear the text from the component before generating again
    password.delete(0, END)


    length = 10
    numbers = "0123456789"
    special_characters = "!@#$%&"
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    choices = ["N", "S", "L"]

    for i in range(length):
        random_choice = random.choice(choices)

        if random_choice =="N":
            random_character = random.choice(numbers)
        elif random_choice == "S":
            random_character = random.choice(special_characters)
        else:
            random_character = random.choice(alphabets)
        
        my_password += random_character
    
    password.insert(0, my_password)

    print(my_password)


# Could have also used terminal for opening but rather used chat gpt to open in the system itself
def show_file():
    open_file_system("data.txt")
    

def clear_all():
    password.delete(0, END)
    user_name.delete(0, END)
    website_name.delete(0, END)

    





add_file_button = Button(text = "Add To File", command=add_to_file)
add_file_button.place(x=80, y=505)

generate_button = Button(text="Generate", command=generate_password)
generate_button.place(x=480, y = 440)

show_file_button = Button(text="Show File", command=show_file)
show_file_button.place(x=250, y= 505)

clear_all_button =Button(text="Clear", command=clear_all)
clear_all_button.place(x=410, y= 505)

root.mainloop()