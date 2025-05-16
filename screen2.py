from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import pandas as pd
import subprocess
from PIL import Image, ImageTk

# Create the main window
window = Tk()
window.title('PROCEED YOUR TRANSACTION SAFELY')
window.geometry('600x600')
window.configure(bg="#f3f3f3")

# Set up background image
img_path = "atm img.jpeg"  # Path to your image
try:
    bg_image = Image.open(img_path)
    bg_photo = ImageTk.PhotoImage(bg_image.resize((600, 600)))
    bg_label = Label(window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
except Exception:
    bg_label = Label(window, text="ATM Background Image", font=("Arial", 20), bg="#f3f3f3")
    bg_label.place(relwidth=1, relheight=1)

# Date and time
now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

# Tabs for SBI and ICICI
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control, style="TFrame")
tab2 = ttk.Frame(tab_control, style="TFrame")
tab_control.add(tab1, text='SBI')
tab_control.add(tab2, text='ICICI')

# Styling for labels and entries
label_font = ("Helvetica", 12, "bold")
entry_bg = "#ffffff"
entry_border = "#cccccc"

# SBI Tab
Label(tab1, text='Amount:', font=label_font).grid(row=0, column=0, pady=10, padx=20)
amount_entry = Entry(tab1, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1)
amount_entry.grid(row=0, column=1, pady=10, padx=10)

Label(tab1, text='To (Account No):', font=label_font).grid(row=1, column=0, pady=10, padx=20)
account_entry = Entry(tab1, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1)
account_entry.grid(row=1, column=1, pady=10, padx=10)

Label(tab1, text='CVV:', font=label_font).grid(row=2, column=0, pady=10, padx=20)
cvv_entry = Entry(tab1, show='*', bg=entry_bg, highlightbackground=entry_border, highlightthickness=1)
cvv_entry.grid(row=2, column=1, pady=10, padx=10)

def complete_transaction():
    if amount_entry.get() and account_entry.get() and cvv_entry.get():
        messagebox.showinfo(
            'Transaction Successful!',
            f'Your transaction of ₹{amount_entry.get()} has been successfully completed!',
            icon='info',
        )
        data = {'Date': [date], 'Time': [time], 'Amount': [amount_entry.get()], 'To': [account_entry.get()]}
        df = pd.DataFrame(data)
        df.to_excel('atm.xlsx', index=False, header=False, mode='a')
    else:
        messagebox.showerror(
            'Error',
            'All fields are required to complete the transaction.',
            icon='error',
        )

Button(tab1, text='Complete Transaction', command=complete_transaction, bg="#0078D7", fg="#ffffff", font=label_font).grid(
    row=3, column=1, pady=20
)

# ICICI Tab
Label(tab2, text='Amount:', font=label_font).grid(row=0, column=0, pady=10, padx=20)
amount_icici = Entry(tab2, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1)
amount_icici.grid(row=0, column=1, pady=10, padx=10)

Label(tab2, text='To (Account No):', font=label_font).grid(row=1, column=0, pady=10, padx=20)
account_icici = Entry(tab2, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1)
account_icici.grid(row=1, column=1, pady=10, padx=10)

Label(tab2, text='CVV:', font=label_font).grid(row=2, column=0, pady=10, padx=20)
cvv_icici = Entry(tab2, show='*', bg=entry_bg, highlightbackground=entry_border, highlightthickness=1)
cvv_icici.grid(row=2, column=1, pady=10, padx=10)

def icici_transaction():
    if amount_icici.get() and account_icici.get() and cvv_icici.get():
        messagebox.showinfo(
            'Transaction Successful!',
            f'Your transaction of ₹{amount_icici.get()} has been successfully completed!',
            icon='info',
        )
        data = {'Date': [date], 'Time': [time], 'Amount': [amount_icici.get()], 'To': [account_icici.get()]}
        df = pd.DataFrame(data)
        df.to_excel('atm.xlsx', index=False, header=False, mode='a')
    else:
        messagebox.showerror(
            'Error',
            'All fields are required to complete the transaction.',
            icon='error',
        )

Button(tab2, text='Complete Transaction', command=icici_transaction, bg="#0078D7", fg="#ffffff", font=label_font).grid(
    row=3, column=1, pady=20
)

# Show Analysis (opens screen3.py)
def show_analysis():
    try:
        subprocess.run(["python", "screen3.py"])
    except FileNotFoundError:
        messagebox.showerror('Error', 'Analysis screen not found.')

Button(tab1, text='Show Analysis', command=show_analysis, bg="#2D89EF", fg="#ffffff", font=label_font).grid(row=4, column=1, pady=10)
Button(tab2, text='Show Analysis', command=show_analysis, bg="#2D89EF", fg="#ffffff", font=label_font).grid(row=4, column=1, pady=10)

# Pack tabs
tab_control.pack(expand=1, fill='both')

# Run main loop
window.mainloop()
