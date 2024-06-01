import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = tkinter.Tk()
reps = 0
checks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
# Dont forget to checks = ""

def reset_timer():
    global checks, timer, reps

    window.after_cancel(timer)
    checks = ""
    reps = 0
    canvas.itemconfig(text_timer, text = "00:00")
    upper_label.config(text="Timer", foreground=GREEN)
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1

    if reps % 8 == 0:
        upper_label.config(text="Long Break", foreground=RED)
        count_down(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        upper_label.config(text="Short Break", foreground=PINK)

        count_down(SHORT_BREAK_MIN * 60)
    else:       
        upper_label.config(text="Work", foreground=GREEN)
        count_down(WORK_MIN * 60)
        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global checks
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)

    #  Dynamic typing 
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(text_timer, text = f"{count_min}:{count_sec}")


    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 != 0:
            checks += "✔"
        start_timer()
        lower_label.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #
window.title("Pomodoro Timer")
window.minsize(height=350, width=400)
window.config(padx=100, pady=100, bg=YELLOW)



# Creating a canvas 
canvas = tkinter.Canvas(width=234, height=230, bg=YELLOW, highlightthickness=0)

tomato_img = tkinter.PhotoImage(file="tomato.png")

canvas.create_image(112, 115, image=tomato_img)
text_timer = canvas.create_text(112, 135, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))


canvas.grid(row=1, column=3)

# Reset button (Right)
reset_button = tkinter.Button(text="Reset", width=10, command=reset_timer)
reset_button.grid(row=2, column=2)

# Start Button (Left)
start_button = tkinter.Button(text="Start", width=10, command=start_timer)
start_button.grid(row=2, column=4)



# Upper label(Timer or start or break)
upper_label = tkinter.Label(text="Timer", font=(FONT_NAME, 80, "bold"), foreground=GREEN, background=YELLOW)
upper_label.grid(row=0, column = 3)



# Lower Label(Total completed pomodoro checkmarks)
lower_label = tkinter.Label(background=YELLOW, font=(FONT_NAME, 15, "bold"), foreground=GREEN)
lower_label.grid(row=3, column = 3)



window.mainloop()