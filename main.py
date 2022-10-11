import sys
from datetime import datetime
import time
from tkinter import *
from time import strftime
from tkinter import messagebox
from tkinter import ttk
from turtle import width

#function to get current time
def get_time():
    string = strftime('%I:%M:%S %p')
    clock.config(text = string)
    now = datetime.now()
    date.config(text=now.strftime('%A %x'))
    root.after(1000, get_time)

#function for timer
def pomodoroTimer():
    timer = focus_time
    type.config(text = 'Get to work!')
    while timer >= 0:
        mins, secs = divmod(timer, 60)
        pomodoro.config(text = '{:02d}:{:02d}'.format(mins, secs))
        timer -=1
        root.update()
        time.sleep(1)
    time.sleep(3)
    breakTimer()


def breakTimer():
    timer = break_time
    type.config(text = 'Take a Break!')
    while timer >= 0:
        mins, secs = divmod(timer, 60)
        pomodoro.config(text = '{:02d}:{:02d}'.format(mins, secs))
        timer -=1
        root.update()
        time.sleep(1)
    time.sleep(3)
    pomodoroTimer()




# root window
root=Tk()
root.title('Clock')
root.geometry('600x300')
root.resizable(0,0)
root.configure(bg='#404040')

#Notebook adds tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(fill="both")

#Setting up frames for notebook
my_frame1 = Frame(my_notebook,width=600,height = 300,bg='#404040')
my_frame2 = Frame(my_notebook,width=600,height = 300,bg='#404040')
my_frame1.pack(fill="both")
my_frame2.pack(fill="both")
my_notebook.add(my_frame1, text="Clock")
my_notebook.add(my_frame2, text="Pomodoro")



#Creating labels for time tab
clock = Label(my_frame1,font = ('Hack', 60, 'bold'),fg='#a0b6f7', bg='#404040',pady=40)
clock.pack(anchor=CENTER)
date = Label(my_frame1,font = ('Hack', 30, 'bold'),pady=150, fg='#f2f261', bg='#404040')
date.pack(anchor=CENTER)
get_time()

#Creating labels for Pomodoro tab
focus_time = 1500
break_time = 300
relax = False
type = Label(my_frame2, font = ('Hack', 40, 'bold'),fg='#a0b6f7', bg='#404040')
type.pack(anchor=N)
pomodoro = Label(my_frame2,font = ('Hack', 40, 'bold'),fg='#a0b6f7', bg='#404040',pady=40)
pomodoro.pack(anchor=CENTER)
start = Button(my_frame2, text="Start", command = pomodoroTimer)
start.place(x=250,y=225)

# Start the app
root.mainloop()