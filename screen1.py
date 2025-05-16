from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import subprocess
from PIL import Image, ImageTk

# Create the main window
window = Tk()
window.title('User Login')
window.geometry('600x600')

# Set the ATM image as background
img_path = "atm img.jpeg"  # Path to your image
bg_image = Image.open(img_path)
bg_photo = ImageTk.PhotoImage(bg_image.resize((650, 650)))  # Resize the image to fit the window
bg_label = Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Make sure the image fills the window

# Styles for modern look
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10, foreground='white', background='blue')
style.configure('TLabel', font=('Helvetica', 12), foreground='white', background='DarkGrey')
style.configure('TEntry', font=('Helvetica', 12), padding=5)
style.configure('TCheckbutton', font=('Helvetica', 10), foreground='white', background='DarkGrey')

# Date and time
now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M")

# Title
title_label = Label(window, text="Secure ATM Login", font=("Arial", 20, "bold"), bg="DarkGrey", fg="white")
title_label.place(x=180, y=50)

# Username and password fields
ttk.Label(window, text='Username:').place(x=150, y=200)
username_entry = ttk.Entry(window)
username_entry.place(x=250, y=200, width=200)

ttk.Label(window, text='Password:').place(x=150, y=250)
password_entry = ttk.Entry(window, show='*')
password_entry.place(x=250, y=250, width=200)

# Checkbox
chk = IntVar()
ttk.Checkbutton(window, text='I am not a robot', variable=chk).place(x=250, y=300)

# Button function
def clicked():
    if username_entry.get() == 'manvendra' and password_entry.get() == '1100' and chk.get() == 1:
        # Success Notification
        success_popup = Toplevel(window)
        success_popup.title("Login Successful")
        success_popup.geometry("300x200")
        success_popup.configure(bg="lightgreen")
        ttk.Label(success_popup, text="Welcome Manvendra!", font=("Helvetica", 14, "bold"), foreground="black").pack(pady=20)
        ttk.Button(success_popup, text="Proceed", command=lambda: [success_popup.destroy(), open_screen2()]).pack(pady=20)
    else:
        messagebox.showerror("Error", "Invalid Credentials or Checkbox Unchecked")

# Open screen2.py
def open_screen2():
    subprocess.run(["python", "screen2.py"])
    window.destroy()  # Close the current window

# Proceed Button
proceed_btn = ttk.Button(window, text='Proceed', command=clicked)
proceed_btn.place(x=250, y=350)

# Run the main loop
window.mainloop()
