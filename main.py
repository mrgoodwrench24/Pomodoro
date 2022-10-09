import sys, tkinter as tk

# root window
root=tk.Tk()
root.title('Pomodoro Timer')
root.geometry('640x370')
root.resizable(True,True)


greeting = tk.Label(root,text="Hello, Tkinter")
greeting.pack()

# Start the app
root.mainloop()