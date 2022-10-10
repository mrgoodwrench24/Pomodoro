import sys
from datetime import datetime
from tkinter import *
from time import strftime
from tkinter import messagebox
from turtle import width

#function to get current time
def time():
    string = strftime('%I:%M:%S %p')
    clock.config(text = string)
    clock.after(200, time)

# root window
root=Tk()
root.title('Clock')
root.geometry('600x300')
root.resizable(0,0)
root.configure(bg='#404040')


clock = Label(root,font = ('times', 60, 'bold'),fg='#a0b6f7', bg='#404040',pady=40)
#clock.grid(row=2, column=2,pady=100,padx=100)
#clock.pack(padx=100,pady=100,expand=True)
clock.pack(anchor=CENTER)
date = Label(root,font = ('times', 30, 'bold'),pady=150, fg='#f2f261', bg='#404040')
now = datetime.now()
date.config(text=now.strftime('%A %x'))
date.pack(anchor=CENTER)
time()

# Start the app
root.mainloop()