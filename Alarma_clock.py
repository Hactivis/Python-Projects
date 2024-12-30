import tkinter
from time import strftime

#  creating the main application window 
top = tkinter.Tk()
top.title("Dynamic Clock") #   Updated title
top.resizable(0,0) #  Making window non-resizable

# Functions to determine the time of day
def get_time_of_day(hour):
    if 5 <= hour < 12:
        return "Morning"
    elif 12 <= hour <18:
        return "Afternoon"
    else:
        return "Evening"
    
# Function to update the time display
def update_time():
    current_time = strftime("%H:%M:%S %p")
    hour = int(strftime("%H"))
    time_of_day = get_time_of_day(hour)

    # update the text of the clocktime Lable with the current time and time of day 
    clock_time.config(text=current_time + f"\nGood {time_of_day}!")

    # Dynamically change the background color based on time of day
    color =(
        "Yellow"
        if time_of_day == "Morning"
        else "lightblue" if time_of_day == "Afternoon" else "lightcoral"

    )
    top.config(background=color)

    # schedule the update_time function to be called again after 1000 milliseconds (1 second)
    clock_time.after(1000, update_time)

# creating a lable widget to display the time 
clock_time = tkinter.Label(
    top,
    font=("courier new", 40),
    background="black",
    foreground="white",
)

# position the Lable widget in the center of the window
clock_time.pack(anchor="center")

#call update time function to updating the time

update_time()

# start the tkinter main loop
top.mainloop()