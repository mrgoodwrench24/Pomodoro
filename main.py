import sys
from tkinter import *
from time import strftime

#function to get current time
def time():
    string = strftime('%I:%M:%S %p')
    clock.config(text = string)
    clock.after(200, time)

# root window
root=Tk()
root.title('Clock')
root.geometry('640x370')
root.resizable(True,True)



clock = Label(root,font = ('times', 60, 'bold'),pady=25, fg='#CCF381', bg='#4831D4')
clock.grid(row=2, column=2,pady=100,padx=100)
#clock.pack(anchor=CENTER)
time()

# Start the app
root.mainloop()