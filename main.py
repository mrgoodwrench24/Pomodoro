import sys
from datetime import datetime
from tkinter import *
from time import strftime
from tkinter import messagebox
from tkinter import ttk
from turtle import width

#function to get current time
def time():
    string = strftime('%I:%M:%S %p')
    clock.config(text = string)
    now = datetime.now()
    date.config(text=now.strftime('%A %x'))
    clock.after(1000, time)
    date.after(1000,time)

# root window
root=Tk()
root.title('Clock')
root.geometry('600x300')
root.resizable(0,0)
root.configure(bg='#404040')

my_notebook = ttk.Notebook(root)
my_notebook.pack()

my_frame1 = Frame(my_notebook,width=600,height = 300,bg='#404040')
my_frame2 = Frame(my_notebook,width=600,height = 300,bg='#404040')

my_frame1.pack(fill="both",expand=1)
my_frame2.pack(fill="both",expand=1)

my_notebook.add(my_frame1, text="Clock")
my_notebook.add(my_frame2, text="Pomodoro")



clock = Label(my_frame1,font = ('times', 60, 'bold'),fg='#a0b6f7', bg='#404040',pady=40)
clock.pack(anchor=CENTER)
date = Label(my_frame1,font = ('times', 30, 'bold'),pady=150, fg='#f2f261', bg='#404040')
date.pack(anchor=CENTER)
time()

# Start the app
root.mainloop()