from re import A
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import *
from random import *
import json
import os

list1 = []
def userGUI(wind):
    root = Toplevel(wind)
    root.geometry("925x500+300+150")
    root.title("Welcome!")
    root.configure(bg="#fff")
    root.resizable(False, False)

    canvas = Canvas(root,width=500,height=500)


    img = ImageTk.PhotoImage(file='vnr2fix2.png')
    Label(root,image=img,bg='white').place(x=50,y=50)

    frame=Frame(root,width=350,height=350,bg="white")
    frame.place(x=480,y=70)

    my_tree = None

    def checking():
        root.destroy()
        root2 = Tk()
        root2.title("Ticket Checker")
        root2.geometry("625x500+300+150")
        root2.configure(bg="#57a8f8")
        root2.resizable(False, False)
        fr = Frame(root2, bg = "#57a8f8")
        fr.pack(pady=40)
        Label(fr,text="Enter your ticket ID: ", font=('Arial',16,'bold'),bg="#57a8f8",fg='#fff').grid(row=0,column=0)
        a1=Entry(fr, font=('Arial',16,'bold'), background="#fff")
        a1.grid(row=2,column=0)
        global list1
        with open(os.getcwd()+'/Data/Ticket.txt', 'r') as f:
            line = f.read()
            lines = line.split("\n")
            for line in lines:
                list1.append(json.loads(line))
        def close():
            root2.destroy()
        def checkTick():
            t = False
            for i in range (len(list1)):
                if a1.get() == list1[i]['Ticket_ID']:
                    print(list1[i])
                    t = True
                    Label(fr,text="Date Available: "+list1[i]['Date Available'], font=('Arial',16,'bold'),bg="#57a8f8",fg='#fff').grid(row=5,column=0)
                    Label(fr,text="Train's ID: "+list1[i]['Train ID'], font=('Arial',16,'bold'),bg="#57a8f8",fg='#fff').grid(row=6,column=0)
                    Label(fr,text="Reservation's  ID: "+list1[i]['Res_ID'], font=('Arial',16,'bold'),bg="#57a8f8",fg='#fff').grid(row=7,column=0)
                    Label(fr,text="Departure Time: "+list1[i]['Departure Time'], font=('Arial',16,'bold'),bg="#57a8f8",fg='#fff').grid(row=8,column=0)
                    Label(fr,text="Departure: "+list1[i]['Departure'], font=('Arial',16,'bold'),bg="#57a8f8",fg='#fff').grid(row=9,column=0)
                    Label(fr,text="Destination: "+list1[i]['Destination'], font=('Arial',16,'bold'),bg="#57a8f8",fg='#fff').grid(row=10,column=0)
                    Label(fr,text="Class: "+list1[i]['Class'], font=('Arial',16,'bold'),bg="#57a8f8",fg='#fff').grid(row=11,column=0)
                    Label(fr,text="Ticket's Type: "+list1[i]['Kind'], font=('Arial',16,'bold'),bg="#57a8f8",fg='#fff').grid(row=12,column=0)
            if t == False:
                messagebox.showerror('Error', 'Ticket not found!')
                t = True
        f.close()
        checking_button=Button(root2,text="   Search   ",font=('Arial',20,'bold'),border=0, bg='white',cursor='hand2', fg='black', command  = lambda:[checkTick()])
        checking_button.pack(pady=10)
        return_button=Button(root2,text="   Return   ",font=('Arial',20,'bold'),border=0, bg='white',cursor='hand2', fg='black',command = lambda:[close(), userGUI(wind)])
        return_button.pack(pady=10)
        root2.mainloop()

    def booking():
        root.destroy()
        root2 = Tk()
        root2.title("Booking")
        root2.geometry("925x500+300+150")
        root2.configure(bg="#57a8f8")
        root2.resizable(False, False)
        fr = Frame(root2, bg = "#57a8f8")
        fr.pack(pady=40)
        train = []
        with open(os.getcwd()+'/Data/Train.txt', 'r') as f:
            line = f.read()
            lines = line.split("\n")
            for line in lines:
                train.append(json.loads(line))
        
        Label(fr,text="From: ", font=('Arial',16,'bold'),bg="#57a8f8",fg='#fff').grid(row=0,column=0)
        c1=Combobox(fr,font=('Arial',16,'bold'),values=["Hà Nội", 'Sài Gòn', 'Huế', 'Đà Nẵng', 'Nha Trang', 'Hải Dương', 'Hải Phòng'])
        c1.grid(row=0,column=1)
        Label(fr,text="To: ",fg='#fff', font=('Arial',16,'bold'),bg="#57a8f8").grid(row=1,column=0)
        c2=Combobox(fr,font=('Arial',16,'bold'),values=["Hà Nội", 'Sài Gòn', 'Huế', 'Đà Nẵng', 'Nha Trang', 'Hải Dương', 'Hải Phòng'])
        c2.grid(row=1,column=1)
        Label(fr,text="Type: ",fg='#fff', font=('Arial',16,'bold'),bg="#57a8f8").grid(row=2,column=0)
        def close():
            root2.destroy()

        def set_value():
            if r.get() == 1:
                cal2["state"] = "disabled"
            else:
                cal2["state"] = "normal"
        r = IntVar()
        r.set("1")
        r1=Radiobutton(fr,text="One-way   ",variable=r, value=1, font=('Arial',16,'bold'), border=1, background="#fff",highlightbackground="#57a8f8", command=set_value)
        r1.grid(row=2,column=1)
        r2=Radiobutton(fr,text="Round Trip",variable=r, value=2, font=('Arial',16,'bold'), border = 1,background="#fff",highlightbackground="#57a8f8",command=set_value)
        r2.grid(row=3,column=1)
        Label(fr,text="Departure date: ",fg='#fff', font=('Arial',16,'bold'),bg="#57a8f8").grid(row=4,column=0)
        cal1=DateEntry(fr, font=('Arial',16,'bold'), background="#fff")
        cal1.grid(row=4,column=1)
        Label(fr,text="Return date: ",fg='#fff', font=('Arial',16,'bold'), bg="#57a8f8").grid(row=5,column=0)
        cal2=DateEntry(fr, font=('Arial',16,'bold'), background="#fff",state=DISABLED)
        cal2.grid(row=5,column=1)
        Label(fr,text="Customer's Name: ",fg='#fff', font=('Arial',16,'bold'),bg="#57a8f8").grid(row=6,column=0)
        
        a1=Entry(fr, font=('Arial',16,'bold'), background="#fff")
        a1.grid(row=6,column=1)
        Label(fr,text="Customer's Identity Card: ",fg='#fff', font=('Arial',16,'bold'),bg="#57a8f8").grid(row=7,column=0)
        a2=Entry(fr, font=('Arial',16,'bold'), background="#fff")
        a2.grid(row=7,column=1)
        Label(fr,text="Customer's Phone: ",fg='#fff', font=('Arial',16,'bold'),bg="#57a8f8").grid(row=8,column=0)
        a3=Entry(fr, font=('Arial',16,'bold'), background="#fff")
        a3.grid(row=8,column=1)
        Label(fr,text="Customer's Email: ",fg='#fff', font=('Arial',16,'bold'),bg="#57a8f8").grid(row=9,column=0)
        a4=Entry(fr, font=('Arial',16,'bold'), background="#fff")
        a4.grid(row=9,column=1)

        Label(fr,text="Customer's Age: ",fg='#fff', font=('Arial',16,'bold'),bg="#57a8f8").grid(row=10,column=0)
        a5=Entry(fr, font=('Arial',16,'bold'), background="#fff")
        a5.grid(row=10,column=1)
        Label(fr,text="Customer's Gender: ",fg='#fff', font=('Arial',16,'bold'),bg="#57a8f8").grid(row=11,column=0)
        a6=Combobox(fr,font=('Arial',16,'bold'),values=['male', 'female', 'others'])
        a6.grid(row=11, column=1)
        # my_tree = ttk.Treeview(root2)
        # my_tree.pack(pady=20)

        # my_tree["columns"] = ("ID", "Name", "Email","Type","Destination","Date")

        # my_tree.column("#0",width=0,stretch=0)
        # my_tree.column("ID",anchor=CENTER,width=100)
        # my_tree.column("Name",anchor=W,width=140)
        # my_tree.column("Email",anchor=W,width=140)
        # my_tree.column("Type",anchor=W,width=140)
        # my_tree.column("Destination",anchor=W,width=140)
        # my_tree.column("Date",anchor=W,width=140)

        # my_tree.heading("#0",text="",anchor=W)
        # my_tree.heading("ID",text="ID",anchor=CENTER)
        # my_tree.heading("Name",text="Name",anchor=W)
        # my_tree.heading("Email",text="Email",anchor=W)
        # my_tree.heading("Type",text="Type",anchor=W)
        # my_tree.heading("Destination",text="Destionation",anchor=W)
        # my_tree.heading("Date",text="Date",anchor=W)

            

        def receipt():
            receipt = Toplevel(root2)
            receipt.title("Receipt")
            
            selected = my_tree.focus()
            values = my_tree.item(selected,"values")
                    
            v1 = c1.get()
            v2 = c2.get()
            v3 = r.get()
                    
            cost = ""
            Label(receipt,text="ID: "+values[0]).pack()
            Label(receipt,text="From: " + v1).pack()
            Label(receipt,text="To: " + v2).pack()
            Label(receipt,text="Time: 6:00 AM or 15:00 PM or 20:00 PM").pack()
            if v3 == 1:
                cost = "25$"
                Label(receipt,text="Type: One-way" ).pack()
                Label(receipt,text="Cost: "+cost).pack()
            else:
                cost = "50$"
                Label(receipt,text="Type: Round trip" ).pack()
                Label(receipt,text="Cost: "+cost).pack()
                    
                    
            def confirm():
                receipt.destroy()            

            cf_button=Button(receipt,text="Confirm",command = confirm)
            cf_button.pack()

        def add_record():
            global count
            global i
            
            if c1.get() == "" or c2.get() == "" or a1.get() =="" or a2.get() =="" or a3.get()=="" or a4.get() =="":
                messagebox.showerror("Error", message = "Opps, you can't leave any field empty")
            else:
                if c1.get() == c2.get():
                    messagebox.showerror("Error",message="Sorry,you can't choose the same city")
                else:
                    messagebox.showinfo("Records",message="Success!")
                    # while i <=999999:
                    #     ticket_id = randint(1,999999)
                    #     i+=1
                    #     break
                    # if r.get() == 1:
                    #     my_tree.insert(parent="",index="end",iid=count,text="",values=(ticket_id,a1.get(),a4.get(),"One-Way",
                    #     c1.get()+"-"+c2.get(),cal1.get()))
                    #     count +=1
                    # else:
                    #     my_tree.insert(parent="",index="end",iid=count,text="",values=(ticket_id,a1.get(),a4.get(),"Round Trip"
                    #     ,c1.get()+"-"+c2.get(),cal1.get()+"-"+cal2.get(),a2.get(),a3.get()))
                    #     count +=1
                a1.delete(0, END)
                a2.delete(0, END)
                a3.delete(0, END)
                a4.delete(0, END)
        def delete():
            x = my_tree.selection()[0]
            my_tree.delete(x)

        

        booking_button=Button(root2,text="    Book    ",font=('Arial',16,'bold'),border=0, bg='white',cursor='hand2', fg='black', command  = lambda:[add_record()])
        booking_button.pack(pady=5)
        recepit_button=Button(root2,text="   Return   ",font=('Arial',16,'bold'),border=0, bg='white',cursor='hand2', fg='black',command = lambda:[close(), userGUI(root)])
        recepit_button.pack(pady=5)
        # details_button = Button(root2, text="Delete",command = delete)
        # details_button.pack(pady=10)
        root2.mainloop()






    Button(frame,text='Book ticket      ', font=('Arial',16,'bold'),fg='white', bg="#57a8f8", width=20, height=2, border=0, cursor='hand2', command=booking).place(x=30, y=87)
    Button(frame,text='Check your ticket', font=('Arial',16,'bold'),fg='white', bg="#57a8f8", width=20, height=2, border=0, cursor='hand2', command=checking).place(x=30, y=150)
    






    root.mainloop()
