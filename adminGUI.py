import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import os
import ast
from tkcalendar import DateEntry


def adminGUI(wind):
    root = Toplevel(wind)
    root.title('Login')
    root.geometry('925x500+300+150')
    root.configure(bg="#fff")
    root.resizable(False, False)

    def signin():
        username = username1.get()
        password = password1.get()

        file=open(os.getcwd()+'/Data/adminsignupdata.txt','r+')
        d=file.read()
        r=ast.literal_eval(d)
        file.close()

        if username in r.keys() and password==r[username]:
            screen=Toplevel(root)
            screen.title("Admin Management")
            screen.geometry('925x500+300+300')
            screen.config(bg="white")
            screen.resizable(False, False)

            frame=Frame(screen,width=600,height=600,bg="white")
            frame.place(x=180,y=40)

            heading=Label(frame,text='Admin Management', fg='#1b46f2', bg="white", font=('Arial', 30, 'bold'))
            heading.place(x=100,y=5)
#========================================button admin function===============================================
            def admin():
                admin=Toplevel(screen)
                admin.title('Admin')
                admin.geometry('1280x720')
                admin.configure(bg="white")
                admin.resizable(False, False)


#============variable=============
                Admin_Name = StringVar()
                ContactAddress = StringVar()
                Admin_Age = IntVar() 
                Admin_ID = StringVar()
                Admin_Email = StringVar()
                Admin_Personal_Email = StringVar()

#=============function============
                def add():
                    if Admin_Name.get()=='' or ContactAddress.get()=='' or Admin_Age.get()==0 or Admin_ID.get()=='' or Admin_Email.get()=='' or Admin_Personal_Email.get()=='':
                        messagebox.showerror('Invalid','All fields must be filled')
                    else:
                        textarea.delete(1.0,END)
                        textarea.insert(END,f'Full name\t\t\t\t{Admin_Name.get()}')
                        textarea.insert(END,f'\nID\t\t\t\t{Admin_ID.get()}')
                        textarea.insert(END,f'\nAge\t\t\t\t{Admin_Age.get()}')
                        textarea.insert(END,f'\nContact address\t\t\t\t{ContactAddress.get()}')
                        textarea.insert(END,f'\nAdmin Email\t\t\t\t{Admin_Email.get()}')
                        textarea.insert(END,f'\nPersonal Email\t\t\t\t{Admin_Personal_Email.get()}')

                def save():
                    data=textarea.get(1.0,END)
                    f1=open('AdminRecords/'+str(Admin_Name.get())+'.txt','w')
                    f1.write(data)
                    f1.close()
                    messagebox.showinfo('Save',f'Admin saved successfully!')

                def reset():
                    textarea.delete(1.0,END)
                    Admin_Name.set('')
                    ContactAddress.set('')
                    Admin_Age.set(0)
                    Admin_ID.set('')
                    Admin_Email.set('') 
                    Admin_Personal_Email.set('')

                def exit():
                    if messagebox.askyesno('Exit','Do you want to exit?'):
                        admin.destroy()
#=============heading=============
                title=Label(admin,text='Admin', bg="#57a8f8", fg='white', font=('Arial', 35,'bold'), relief=GROOVE, bd=0)
                title.pack(fill=X)

#=============admin left manage frame====================
                F1=Frame(admin,bg="#57a8f8", relief=RIDGE,bd=1)
                F1.place(x=10,y=80,width=650,height=530)

                lbl_name=Label(F1,text='Full name ', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_name.grid(row=0,column=0,padx=30,pady=10)
                txt_name=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=20, textvariable=Admin_Name)
                txt_name.grid(row=0,column=1,pady=10,sticky='w')

                lbl_ID=Label(F1,text='ID', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_ID.grid(row=1,column=0,padx=30,pady=10)
                txt_ID=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=10, textvariable=Admin_ID)
                txt_ID.grid(row=1,column=1,pady=10,sticky='w')

                lbl_age=Label(F1,text='Age', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_age.grid(row=2,column=0,padx=30,pady=10)
                txt_age=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=10, textvariable=Admin_Age)
                txt_age.grid(row=2,column=1,pady=10,sticky='w')

                lbl_address=Label(F1,text='Contact address', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_address.grid(row=3, column=0,padx=30,pady=10)
                txt_address=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=20, textvariable=ContactAddress)
                txt_address.grid(row=3,column=1,pady=10,sticky='w')

                lbl_ademail=Label(F1,text='Admin email', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_ademail.grid(row=4, column=0,padx=30,pady=10)
                txt_ademail=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=20, textvariable=Admin_Email)
                txt_ademail.grid(row=4,column=1,pady=10,sticky='w')

                lbl_peremail=Label(F1,text='Personal email ', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_peremail.grid(row=5, column=0,padx=30,pady=10)
                txt_peremail=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=20, textvariable=Admin_Personal_Email)
                txt_peremail.grid(row=5,column=1,pady=10,sticky='w')
#==============admin right show franme===================
                F2=Frame(admin,bg="#57a8f8", relief=RIDGE,bd=1)
                F2.place(x=665,y=80,width=610,height=530)

                lbl_t=Label(F2,text='Admin record', font=('Arial',15), bg="#57a8f8", fg='white',relief=GROOVE)
                lbl_t.pack(fill=X)
                scrol=Scrollbar(F2,orient=VERTICAL)
                scrol.pack(side=RIGHT,fill=Y)
                textarea= Text(F2,font='Arial 15',yscrollcommand=scrol.set)
                textarea.pack(fill=BOTH)
                scrol.config(command=textarea.yview)

#=============admin buttons==============================
                F3=Frame(admin,bg="#57a8f8", relief=RIDGE,bd=1)
                F3.place(x=10,y=615,width=1260,height=100)

                btn1=Button(F3,text='Add', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=add)
                btn1.grid(row=0,column=4,padx=20,pady=7)

                btn2=Button(F3,text='Save', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=save)
                btn2.grid(row=0,column=5,padx=20,pady=7)

                btn3=Button(F3,text='Reset', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=reset)
                btn3.grid(row=0,column=6,padx=20,pady=7)

                btn4=Button(F3,text='Exit', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=exit)
                btn4.grid(row=0,column=7,padx=20,pady=7)

                admin.mainloop()


#========================================button function===============================================
           
            Button(frame,text='Admin', font=('Arial',16,'bold'),fg='white', bg="#16b0f8", width=10, height=1, border=0, cursor='hand2', command=admin).place(x=210, y=107)

#========================================button Customer function===============================================
            def customer():
                customer=Toplevel(screen)
                customer.title('Customer')
                customer.geometry('1280x720')
                customer.configure(bg="white")
                customer.resizable(False, False)


#============variable=============
                Customer_Name = StringVar()
                Customer_Gender = StringVar()
                Customer_Age = IntVar()
                Customer_ID = StringVar()
                Customer_Email = StringVar()

#=============function============
                def add():
                    if Customer_Name.get()=='' or Customer_Gender.get()=='' or Customer_Age.get()==0 or Customer_ID.get()=='' or Customer_Email.get()=='':
                        messagebox.showerror('Invalid','All fields must be filled')
                    else:  
                        textarea.delete(1.0,END)
                        textarea.insert(END,f'Full name\t\t\t\t{Customer_Name.get()}')
                        textarea.insert(END,f'\nID\t\t\t\t{Customer_ID.get()}')
                        textarea.insert(END,f'\nAge\t\t\t\t{Customer_Age.get()}')
                        textarea.insert(END,f'\nGender\t\t\t\t{Customer_Gender.get()}')
                        textarea.insert(END,f'\nCustomer Email\t\t\t\t{Customer_Email.get()}')

                def save():
                    data=textarea.get(1.0,END)
                    f1=open('CustomerRecords/'+str(Customer_Name.get())+'.txt','w')
                    f1.write(data)
                    f1.close()
                    messagebox.showinfo('Save',f'Customer saved successfully!')
                    

                def reset():
                    textarea.delete(1.0,END)
                    Customer_Name.set('')
                    Customer_Gender.set('')
                    Customer_Age.set(0)
                    Customer_ID.set('')
                    Customer_Email.set('') 

                def exit():
                    if messagebox.askyesno('Exit','Do you want to exit?'):
                        customer.destroy()
#=============heading=============
                title=Label(customer,text='Customer', bg="#57a8f8", fg='white', font=('Arial', 35,'bold'), relief=GROOVE, bd=0)
                title.pack(fill=X)

#=============customer left manage frame====================
                F1=Frame(customer,bg="#57a8f8", relief=RIDGE,bd=1)
                F1.place(x=10,y=80,width=650,height=530)

                lbl_name=Label(F1,text='Full name ', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_name.grid(row=0,column=0,padx=30,pady=10)
                txt_name=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=20, textvariable=Customer_Name)
                txt_name.grid(row=0,column=1,pady=10,sticky='w')

                lbl_ID=Label(F1,text='ID', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_ID.grid(row=1,column=0,padx=30,pady=10)
                txt_ID=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=10, textvariable=Customer_ID)
                txt_ID.grid(row=1,column=1,pady=10,sticky='w')

                lbl_age=Label(F1,text='Age', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_age.grid(row=2,column=0,padx=30,pady=10)
                txt_age=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=10, textvariable=Customer_Age)
                txt_age.grid(row=2,column=1,pady=10,sticky='w')

                lbl_gender=Label(F1,text='Gender', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_gender.grid(row=3, column=0,padx=30,pady=10)
                combo_gender=ttk.Combobox(F1,font=('Helvetica',18),state='readonly',textvariable=Customer_Gender)
                combo_gender['value']=('Male', 'Female', 'Others')
                combo_gender.grid(row=3,column=1,pady=10)

                lbl_cusemail=Label(F1,text='Customer email', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_cusemail.grid(row=4, column=0,padx=30,pady=10)
                txt_cusemail=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=20, textvariable=Customer_Email)
                txt_cusemail.grid(row=4,column=1,pady=10,sticky='w')

#==============customer right show franme===================
                F2=Frame(customer,bg="#57a8f8", relief=RIDGE,bd=1)
                F2.place(x=665,y=80,width=610,height=530)

                lbl_t=Label(F2,text='Customer record', font=('Arial',15), bg="#57a8f8", fg='white',relief=GROOVE)
                lbl_t.pack(fill=X)
                scrol=Scrollbar(F2,orient=VERTICAL)
                scrol.pack(side=RIGHT,fill=Y)
                textarea= Text(F2,font='Arial 15',yscrollcommand=scrol.set)
                textarea.pack(fill=BOTH)
                scrol.config(command=textarea.yview)

#=============customer buttons==============================
                F3=Frame(customer,bg="#57a8f8", relief=RIDGE,bd=1)
                F3.place(x=10,y=615,width=1260,height=100)

                btn1=Button(F3,text='Add', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=add)
                btn1.grid(row=0,column=4,padx=20,pady=7)

                btn2=Button(F3,text='Save', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=save)
                btn2.grid(row=0,column=5,padx=20,pady=7)

                btn3=Button(F3,text='Reset', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=reset)
                btn3.grid(row=0,column=7,padx=20,pady=7)

                btn4=Button(F3,text='Exit', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=exit)
                btn4.grid(row=0,column=8,padx=20,pady=7)

                customer.mainloop()
#========================================button function===============================================

            Button(frame,text='Customer', font=('Arial',16,'bold'),fg='white', bg="#177cf4", width=10, height=1, border=0, cursor='hand2', command=customer).place(x=210, y=177)
#=========================================button Ticket=======================================================================
            def ticket():
                ticket=Toplevel(screen)
                ticket.title('Ticket')
                ticket.geometry('1280x720')
                ticket.configure(bg="white")
                ticket.resizable(False, False)


#============variable=============
                Ticket_ID = StringVar()
                Date_Available =  StringVar()
                Train_ID = StringVar() 
                Res_ID = StringVar()
                DepartureTime = StringVar()  
                LandingTime= StringVar()
                Class= StringVar()
                Departure= StringVar()
                Destination= StringVar()
                Kind=StringVar()

                tickets=[]

                id=Ticket_ID.get()
                date=Date_Available.get()
                train=Train_ID.get()
                res=Res_ID.get()
                deptime=DepartureTime.get()
                landtime=LandingTime.get()
                clas=Class.get()
                dep=Departure.get()
                des=Destination.get()
                k=Kind.get()
                tickets.append({
                    "Ticket_ID":id,
                    "Date_Available":date,
                    "Train_ID": train,
                    "Res_ID":res,
                    "DepartureTime": deptime,
                    "LandingTime": landtime,
                    "Class": clas,
                    "Departure": dep,
                    "Destination":des,
                    "Kind":k
                })
               
#=============function============
                def add():
                    if Ticket_ID.get()=='' or Date_Available.get()=='' or Train_ID.get()=='' or Res_ID.get()=='' or DepartureTime.get()=='' or LandingTime.get()=='' or Class.get()=='' or Departure.get()=='' or Destination.get()=='' or Kind.get()=='':
                        messagebox.showerror('Invalid','All fields must be filled')

                    else:
                        id=Ticket_ID.get()
                        date=Date_Available.get()
                        train=Train_ID.get()
                        res=Res_ID.get()
                        deptime=DepartureTime.get()
                        landtime=LandingTime.get()
                        clas=Class.get()
                        dep=Departure.get()
                        des=Destination.get()
                        k=Kind.get()
                        tickets.append({
                            "Ticket_ID":id,
                            "Date_Available":date,
                            "Train_ID": train,
                            "Res_ID":res,
                            "DepartureTime": deptime,
                            "LandingTime": landtime,
                            "Class": clas,
                            "Departure": dep,
                            "Destination":des,
                            "Kind":k
                        })
                        return tickets
                        textarea.delete(1.0,END)
                        for t in tickets:
                            textarea.insert(END, t + '\n')

                def save():
                    data=textarea.get(1.0,END)
                    f1=open('Ticket.txt','w')
                    f1.write(data)
                    f1.close()
                    messagebox.showinfo('Save',f'Ticket saved successfully!')
                    

                def reset():
                    textarea.delete(1.0,END)
                    Ticket_ID.set('')
                    Date_Available.set('')
                    Train_ID.set('')
                    Res_ID.set('')
                    DepartureTime.set('')
                    LandingTime.set('')
                    Class.set('')
                    Departure.set('')
                    Destination.set('')
                    Kind.set('')

                def exit():
                    if messagebox.askyesno('Exit','Do you want to exit?'):
                        ticket.destroy()
#=============heading=============
                title=Label(ticket,text='Ticket', bg="#57a8f8", fg='white', font=('Arial', 35,'bold'), relief=GROOVE, bd=0)
                title.pack(fill=X)

#=============ticket left manage frame====================
                F1=Frame(ticket,bg="#57a8f8", relief=RIDGE,bd=1)
                F1.place(x=10,y=80,width=650,height=530)

                lbl_Ticket_ID=Label(F1,text='Ticket ID', font=('Arial',15,'bold'), bg="#57a8f8", fg='white')
                lbl_Ticket_ID.grid(row=0,column=0,padx=30,pady=10)
                txt_Ticket_ID=Entry(F1,font=('Helvetica',15,'bold'),relief=RIDGE,bd=0, width=10, textvariable=Ticket_ID)
                txt_Ticket_ID.grid(row=0,column=1,pady=10,sticky='w')

                lbl_Date_Available=Label(F1,text='Date Available', font=('Arial',15,'bold'), bg="#57a8f8", fg='white')
                lbl_Date_Available.grid(row=1,column=0,padx=30,pady=10)
                cal_Date_Available=DateEntry(F1, selectmode='day', textvariable=Date_Available)
                cal_Date_Available.grid(row=1,column=1,pady=10,sticky='w')

                lbl_Train_ID=Label(F1,text='Train ID', font=('Arial',15,'bold'), bg="#57a8f8", fg='white')
                lbl_Train_ID.grid(row=2,column=0,padx=30,pady=10)
                txt_Train_ID=Entry(F1,font=('Helvetica',15,'bold'),relief=RIDGE,bd=0, width=10, textvariable=Train_ID)
                txt_Train_ID.grid(row=2,column=1,pady=10,sticky='w')

                lbl_Res_ID=Label(F1,text='Res ID', font=('Arial',15,'bold'), bg="#57a8f8", fg='white')
                lbl_Res_ID.grid(row=3,column=0,padx=30,pady=10)
                txt_Res_ID=Entry(F1,font=('Helvetica',15,'bold'),relief=RIDGE,bd=0, width=10, textvariable=Res_ID)
                txt_Res_ID.grid(row=3,column=1,pady=10,sticky='w')

                lbl_DepartureTime=Label(F1,text='Departure Time', font=('Arial',15,'bold'), bg="#57a8f8", fg='white')
                lbl_DepartureTime.grid(row=4,column=0,padx=30,pady=10)
                txt_DepartureTime=Entry(F1,font=('Helvetica',15,'bold'),relief=RIDGE,bd=0, width=15, textvariable=DepartureTime)
                txt_DepartureTime.grid(row=4,column=1,pady=10,sticky='w')

                lbl_LandingTime=Label(F1,text='Landing Time', font=('Arial',15,'bold'), bg="#57a8f8", fg='white')
                lbl_LandingTime.grid(row=5,column=0,padx=30,pady=10)
                txt_LandingTime=Entry(F1,font=('Helvetica',15,'bold'),relief=RIDGE,bd=0, width=15, textvariable=LandingTime)
                txt_LandingTime.grid(row=5,column=1,pady=10,sticky='w')

                lbl_Class=Label(F1,text='Class', font=('Arial',15,'bold'), bg="#57a8f8", fg='white')
                lbl_Class.grid(row=6, column=0,padx=30,pady=10)
                combo_Class=ttk.Combobox(F1,font=('Helvetica',15), width=10, state='readonly',textvariable=Class)
                combo_Class['value']=('1e', '2e')
                combo_Class.grid(row=6,column=1,pady=10)
                
                lbl_Departure=Label(F1,text='Departure', font=('Arial',15,'bold'), bg="#57a8f8", fg='white')
                lbl_Departure.grid(row=7, column=0,padx=30,pady=10)
                combo_Departure=ttk.Combobox(F1,font=('Helvetica',15), width=10, state='readonly',textvariable=Departure)
                combo_Departure['value']=('Ha Noi', 'Sai Gon', 'Hue', 'Da Nang', 'Nha Trang', 'Hai Duong', 'Hai Phong')
                combo_Departure.grid(row=7,column=1,pady=10)

                lbl_Destination=Label(F1,text='Departure', font=('Arial',15,'bold'), bg="#57a8f8", fg='white')
                lbl_Destination.grid(row=8, column=0,padx=30,pady=10)
                combo_Destination=ttk.Combobox(F1,font=('Helvetica',15), width=10, state='readonly',textvariable=Destination)
                combo_Destination['value']=('Ha Noi', 'Sai Gon', 'Hue','Da Nang', 'Nha Trang', 'Hai Duong', 'Hai Phong')
                combo_Destination.grid(row=8,column=1,pady=10)

                lbl_Kind=Label(F1,text='Kind', font=('Arial',15,'bold'), bg="#57a8f8", fg='white')
                lbl_Kind.grid(row=9, column=0,padx=30,pady=10)
                combo_Kind=ttk.Combobox(F1,font=('Helvetica',15), width=10, state='readonly',textvariable=Kind)
                combo_Kind['value']=('One-way', 'Round-trip')
                combo_Kind.grid(row=9,column=1,pady=10)

#==============ticket right show franme===================
                F2=Frame(ticket,bg="#57a8f8", relief=RIDGE,bd=1)
                F2.place(x=665,y=80,width=610,height=530)

                lbl_t=Label(F2,text='ticket record', font=('Arial',15), bg="#57a8f8", fg='white',relief=GROOVE)
                lbl_t.pack(fill=X)
                scrol=Scrollbar(F2,orient=VERTICAL)
                scrol.pack(side=RIGHT,fill=Y)
                textarea= Text(F2,font='Arial 15',yscrollcommand=scrol.set)
                textarea.pack(fill=BOTH)
                scrol.config(command=textarea.yview)

#=============ticket buttons==============================
                F3=Frame(ticket,bg="#57a8f8", relief=RIDGE,bd=1)
                F3.place(x=10,y=615,width=1260,height=100)

                btn1=Button(F3,text='Add', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=add)
                btn1.grid(row=0,column=4,padx=20,pady=7)

                btn2=Button(F3,text='Save', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=save)
                btn2.grid(row=0,column=5,padx=20,pady=7)

                btn3=Button(F3,text='Reset', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=reset)
                btn3.grid(row=0,column=6,padx=20,pady=7)

                btn4=Button(F3,text='Exit', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=exit)
                btn4.grid(row=0,column=7,padx=20,pady=7)

                ticket.mainloop()
#=========================================button Ticket=======================================================================
            #Button(frame,text='Ticket', font=('Arial',16,'bold'),fg='white', bg="#1b46f2", width=10, height=1, border=0, cursor='hand2', command=ticket).place(x=210, y=317)
#========================================button Worker function===============================================
            def worker():
                worker=Toplevel(screen)
                worker.title('Worker')
                worker.geometry('1280x720')
                worker.configure(bg="white")
                worker.resizable(False, False)


#============variable=============
                Worker_Name= StringVar()
                Worker_ID = StringVar()
                Worker_Age = IntVar()
                Worker_Gender = StringVar() 
                Worker_phonenumber = StringVar()
                shift = StringVar()  
                Job = StringVar()
                driverlicense= StringVar()


        #=============function============
                def add():
                    if Worker_Name.get()=='' or Worker_Gender.get()=='' or Worker_Age.get()==0 or Worker_ID.get()=='' or Worker_phonenumber.get()=='' or shift.get()=='' or Job.get()=='' or driverlicense.get()=='':
                        messagebox.showerror('Invalid','All fields must be filled')
                    else:  
                        textarea.delete(1.0,END)
                        textarea.insert(END,f'Full name\t\t\t\t{Worker_Name.get()}')
                        textarea.insert(END,f'\nID\t\t\t\t{Worker_ID.get()}')
                        textarea.insert(END,f'\nAge\t\t\t\t{Worker_Age.get()}')
                        textarea.insert(END,f'\nGender\t\t\t\t{Worker_Gender.get()}')
                        textarea.insert(END,f'\nPhonenumber\t\t\t\t{Worker_phonenumber.get()}')
                        textarea.insert(END,f'\nShift\t\t\t\t{shift.get()}')
                        textarea.insert(END,f'\nJob\t\t\t\t{Job.get()}')
                        textarea.insert(END,f'\nDriving lisence\t\t\t\t{driverlicense.get()}')

                def save():
                    data=textarea.get(1.0,END)
                    f1=open('WorkerRecords/'+str(Worker_Name.get())+'.txt','w')
                    f1.write(data)
                    f1.close()
                    messagebox.showinfo('Save',f'Worker saved successfully!')
                    

                def reset():
                    textarea.delete(1.0,END)
                    Worker_Name.set('')
                    Worker_ID.set('')
                    Worker_Age.set(0)
                    Worker_Gender.set('')
                    Worker_phonenumber.set('')
                    shift.set('')
                    Job.set('')
                    driverlicense.set('')

                def exit():
                    if messagebox.askyesno('Exit','Do you want to exit?'):
                        worker.destroy()
        #=============heading=============
                title=Label(worker,text='Worker', bg="#57a8f8", fg='white', font=('Arial', 35,'bold'), relief=GROOVE, bd=0)
                title.pack(fill=X)

        #=============worker left manage frame====================
                F1=Frame(worker,bg="#57a8f8", relief=RIDGE,bd=1)
                F1.place(x=10,y=80,width=650,height=530)

                lbl_name=Label(F1,text='Full name ', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_name.grid(row=0,column=0,padx=30,pady=10)
                txt_name=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=20, textvariable=Worker_Name)
                txt_name.grid(row=0,column=1,pady=10,sticky='w')

                lbl_ID=Label(F1,text='ID', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_ID.grid(row=1,column=0,padx=30,pady=10)
                txt_ID=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=10, textvariable=Worker_ID)
                txt_ID.grid(row=1,column=1,pady=10,sticky='w')

                lbl_age=Label(F1,text='Age', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_age.grid(row=2,column=0,padx=30,pady=10)
                txt_age=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=10, textvariable=Worker_Age)
                txt_age.grid(row=2,column=1,pady=10,sticky='w')

                lbl_gender=Label(F1,text='Gender', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_gender.grid(row=3, column=0,padx=30,pady=10)
                combo_gender=ttk.Combobox(F1,font=('Helvetica',18),state='readonly',textvariable=Worker_Gender)
                combo_gender['value']=('Male', 'Female', 'Others')
                combo_gender.grid(row=3,column=1,pady=10)

                lbl_phonenumber=Label(F1,text='Phonenumber', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_phonenumber.grid(row=4,column=0,padx=30,pady=10)
                txt_phonenumber=Entry(F1,font=('Helvetica',20,'bold'),relief=RIDGE,bd=0, width=15, textvariable=Worker_phonenumber)
                txt_phonenumber.grid(row=4,column=1,pady=10,sticky='w')

                lbl_shift=Label(F1,text='Shift', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_shift.grid(row=5, column=0,padx=30,pady=10)
                combo_shift=ttk.Combobox(F1,font=('Helvetica',18), width=10, state='readonly',textvariable=shift)
                combo_shift['value']=('1', '2', '3')
                combo_shift.grid(row=5,column=1,pady=10)

                lbl_job=Label(F1,text='Job', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_job.grid(row=6, column=0,padx=30,pady=10)
                combo_job=ttk.Combobox(F1,font=('Helvetica',18), width=10, state='readonly',textvariable=Job)
                combo_job['value']=('Cleaner', 'Trainman', 'Railroader')
                combo_job.grid(row=6,column=1,pady=10)

                lbl_drivelis=Label(F1,text='Driving Lisence', font=('Arial',20,'bold'), bg="#57a8f8", fg='white')
                lbl_drivelis.grid(row=7, column=0,padx=30,pady=10)
                combo_drivelis=ttk.Combobox(F1,font=('Helvetica',18), width=10, state='readonly',textvariable=driverlicense)
                combo_drivelis['value']=('Yes', 'No')
                combo_drivelis.grid(row=7,column=1,pady=10)


#==============worker right show franme===================
                F2=Frame(worker,bg="#57a8f8", relief=RIDGE,bd=1)
                F2.place(x=665,y=80,width=610,height=530)

                lbl_t=Label(F2,text='worker record', font=('Arial',15), bg="#57a8f8", fg='white',relief=GROOVE)
                lbl_t.pack(fill=X)
                scrol=Scrollbar(F2,orient=VERTICAL)
                scrol.pack(side=RIGHT,fill=Y)
                textarea= Text(F2,font='Arial 15',yscrollcommand=scrol.set)
                textarea.pack(fill=BOTH)
                scrol.config(command=textarea.yview)

#=============worker buttons==============================
                F3=Frame(worker,bg="#57a8f8", relief=RIDGE,bd=1)
                F3.place(x=10,y=615,width=1260,height=100)

                btn1=Button(F3,text='Add', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=add)
                btn1.grid(row=0,column=4,padx=20,pady=7)

                btn2=Button(F3,text='Save', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=save)
                btn2.grid(row=0,column=5,padx=20,pady=7)

                btn3=Button(F3,text='Reset', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=reset)
                btn3.grid(row=0,column=7,padx=20,pady=7)

                btn4=Button(F3,text='Exit', font='arial 20 bold', bg='white', fg='#57a8f8', width=10, command=exit)
                btn4.grid(row=0,column=8,padx=20,pady=7)

                worker.mainloop()
#========================================button Worker function===============================================
            Button(frame,text='Worker', font=('Arial',16,'bold'),fg='white', bg="#1b68f2", width=10, height=1, border=0, cursor='hand2', command=worker).place(x=210, y=247)


            screen.mainloop()

        else:
            messagebox.showerror("Invalid", "Invalid User ID/email or password")


###############################################################################################################################################
        
    def signup_command():
        window=Toplevel(root)
        window.title("SignUp")
        window.geometry('925x500+300+150')
        window.configure(bg="#fff")
        window.resizable(False, False)

        def sign_up():
            username = username1.get()
            password = password1.get()
            confirmpassword = confirm.get()

            if password==confirmpassword:
                try:
                    file=open(os.getcwd()+'/Data/adminsignupdata.txt','r+')
                    d=file.read()
                    r=ast.literal_eval(d)

                    dict2={username:password}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()

                    file=open(os.getcwd()+'/Data/adminsignupdata.txt','w')
                    w=file.write(str(r))

                    messagebox.showinfo('Sign Up', 'Sucessfully sign up!')

                except:
                    file=open(os.getcwd()+'/Data/adminsignupdata.txt','w')
                    pp=str({'username':'password'})
                    file.write(pp)
                    file.close()

            else:
                messagebox.showerror('Invalid',"Both password should match!")
        def sign():
            window.destroy()

        img = ImageTk.PhotoImage(file='vnr2fix2.png')
        Label(window,image=img,border=0,bg='white').place(x=50,y=90)

        frame=Frame(window,width=350,height=390,bg="white")
        frame.place(x=480,y=50)

        heading=Label(frame,text='Sign up', fg='#57a8f8', bg="white", font=('Arial', 30, 'bold'))
        heading.place(x=100,y=5)
    
#=========================================================================================================================
        def on_enter(e):
            username1.delete(0,'end')
        
        def on_leave(e):
            name=username1.get()
            if name=='':
                username1.insert(0,'UsernameID/Email')

        username1 = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
        username1.place(x=30,y=80)
        username1.insert(0,'User ID/Email')
        username1.bind('<FocusIn>', on_enter)
        username1.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25,y=107)

#=========================================================================================================================

        def on_enter(e):
            password1.delete(0,'end')
            password1.insert(0,'')
            
        
        def on_leave(e):
            name=password1.get()
            if name=='':
                password1.insert(0,'Password')

        password1 = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
        password1.place(x=30,y=150)
        password1.insert(0,'Password')
        password1.bind('<FocusIn>', on_enter)
        password1.bind('<FocusOut>', on_leave)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#=========================================================================================================================
        def on_enter(e):
            confirm.delete(0,'end')
        
        def on_leave(e):
            name=confirm.get()
            if name=='':
                confirm.insert(0,'Confirm password')

        confirm = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
        confirm.place(x=30,y=220)
        confirm.insert(0,'Confirm password')
        confirm.bind('<FocusIn>', on_enter)
        confirm.bind('<FocusOut>', on_leave)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

#=========================================================================================================================

        Button(frame, width=39,pady=7,text='Sign up', bg='#5785f8',fg='white',border=0,command=sign_up).place(x=25,y=280)
        label=Label(frame,text="Have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label.place(x=90,y=340)

        signin= Button(frame,width=6,text='Log in', border=0, bg='white',cursor='hand2', fg='#5785f8',command=sign)
        signin.place(x=210,y=337)

        window.mainloop()

##############################################################################################################################################

    img = ImageTk.PhotoImage(file='vnr2fix2.png')
    Label(root,image=img,bg='white').place(x=50,y=50)

    frame=Frame(root,width=350,height=350,bg="white")
    frame.place(x=480,y=70)

    heading=Label(frame,text='Log in', fg='#57a8f8', bg="white", font=('Arial', 30, 'bold'))
    heading.place(x=100,y=5)

#=========================================================================================================================
    def on_enter(e):
        username1.delete(0,'end')
        
    def on_leave(e):
        name=username1.get()
        if name=='':
            username1.insert(0,'User ID/Email')

    username1 = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    username1.place(x=30,y=80)
    username1.insert(0,'User ID/Email')
    username1.bind('<FocusIn>', on_enter)
    username1.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25,y=107)
#=========================================================================================================================

    def on_enter(e):
        password1.delete(0,'end')
        
    def on_leave(e):
        name=password1.get()
        if name=='':
            password1.insert(0,'Password')

    password1 = Entry(frame, width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    password1.place(x=30,y=150)
    password1.insert(0,'Password')
    password1.bind('<FocusIn>', on_enter)
    password1.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#=========================================================================================================================

    Button(frame, width=39,pady=7,text='Log in', bg='#5785f8',fg='white',border=0,command=signin).place(x=25,y=204)
    # label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    # label.place(x=75,y=270)

    # sign_up= Button(frame,width=6,text='Sign up', border=0, bg='white',cursor='hand2', fg='#5785f8',command=signup_command)
    # sign_up.place(x=235,y=267)


    root.mainloop()
