from adminGUI import *
from tkinter import *
from userGUI import *

wind = Tk()
wind.title('Welcome to VNR')
wind.geometry('925x500+300+150')
wind.configure(bg="#fff")
wind.resizable(False, False)

def AdminGUI(wind):
    adminGUI(wind)

def GuestGUI(wind):
    userGUI(wind)

def close():
    wind.destroy()

frame=Frame(wind,width=600,height=600,bg="white")
frame.place(x=180,y=40)

Button(frame, text = "Admin login",font=('Arial',18,'bold'),fg='white', bg="#57a8f8", width=20, height=2, border=0, cursor='hand2', command=lambda:[ AdminGUI(wind)]).place(x=125, y=87)
Button(frame, text = "Guest login", font=('Arial',18,'bold'),fg='white', bg="#57a8f8", width=20, height=2, border=0, cursor='hand2', command =lambda: [GuestGUI(wind)]).place(x=125, y=167)

wind.mainloop()
h
