#screen 1
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pandas as pd
df = pd.read_excel("atm.xlsx")

now=datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")




window=Tk()
window.title('PLEASE LOGIN TO PROCEEDb')
window.geometry('450x500')
lb=Label(window,text='\n\n\n\n\n\n\n\n\n\t\t').grid(row=0,column=0)
lbl1=Label(window,text='username',bg='DarkGrey',font=('Arial',10)).grid(row=1,column=1)
lbl1=Entry(window)
lbl1.grid(row=1,column=2)

lb=Label(window,text='\n\t').grid(row=2,column=0)


lbl2=Label(window,text='password',bg='DarkGrey',font=('Arial',10)).grid(row=3,column=1)
lbl2=Entry(window)
lbl2.grid(row=3,column=2)

# checkbox
def clicked():
    if (chk.get()==1):
        #adding login credentials to txt file
        print(date)
        print(time)
        fh=open("atm.txt","a")
        x='username: %s\npassword: %s'%(lbl1.get(),lbl2.get())
        fh.write(x)
        fh.write('\n')
        fh.close()
        ##############
        #adding to excel file
        
        
        
    else:
        messagebox.showinfo('oops', 'please fill the checkbox properly')
        
chk=IntVar()
ch=Checkbutton(window,text='I AM NOT A ROBOT',variable=chk).grid(row=4,column=3)


        

btn=Button(window,text='click here',command=clicked).grid(row=4,column=2)





