from tkinter import Tk, Frame, LabelFrame, Label, Entry, IntVar, Radiobutton, Button, messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk
from dars.database import Database

windows = Tk()
windows.geometry("800x640")
windows.configure(bg="#826BFB")
db = Database()

register_photo = ImageTk.PhotoImage(file="19 dars/register.png")
register_label = Label(windows, image=register_photo)
register_label.place(x=560, y=300)

user_photo = ImageTk.PhotoImage(file="user.png")
user_label = Label(windows, image=user_photo)
user_label.place(x=560, y=130)

frame = Frame(windows)
frame.grid(padx=30, pady=30)

label_frame = LabelFrame(frame)
label_frame.grid()


def register_func():
    fullname = fullname_entry.get()
    email = email_entry.get()
    phone = phone_number_entry.get()
    birth = birth_date_entry.get()

    if fullname and email and phone and birth:
        db.insert_user(full_name=fullname, email=email, phone=phone, birht=birth)
        messagebox.showinfo(title="Saqlandi !",
                            message="Siz muvaffaqiyatli ro'yhatdan o'tdingiz !")
    else:
        messagebox.showerror(title="Xato",
                             message="Noto'g'ri kiritish !")


# 1 chi qator ------------------------------------------------
registration_label = Label(label_frame,
                           text="Registration Form",
                           font=("Arial", 30))
registration_label.grid(row=0, column=0, columnspan=2, sticky="news")

# 2 chi qator ------------------------------------------------
fullname_label = Label(label_frame,
                       text="Fullname",
                       font=("Calibri", 15))
fullname_label.grid(row=1, column=0)
fullname_entry = Entry(label_frame, width=70)
fullname_entry.grid(row=2, column=0, ipady=7, columnspan=2, sticky="news")

# 3 chi qator ------------------------------------------------
email_label = Label(label_frame,
                       text="Email",
                       font=("Calibri", 15))
email_label.grid(row=3, column=0)
email_entry = Entry(label_frame, width=70)
email_entry.grid(row=4, column=0, ipady=7, columnspan=2, sticky="news")

# 4 chi qator ------------------------------------------------
phone_number_label = Label(label_frame,
                       text="Phone_number",
                       font=("Calibri", 15))
phone_number_label.grid(row=5, column=0)
phone_number_entry = Entry(label_frame, width=30)
phone_number_entry.grid(row=6, column=0, ipady=7)

birth_date_label = Label(label_frame,
                       text="Birth Date",
                       font=("Calibri", 15))
birth_date_label.grid(row=5, column=1)
birth_date_entry = Entry(label_frame, width=30)
birth_date_entry.grid(row=6, column=1, ipady=7)

# 5 chi qator ------------------------------------------------
gender_label = Label(label_frame,
                       text="Gender",
                       font=("Calibri", 15))
gender_label.grid(row=7, column=0)

var = IntVar()
radio_male = Radiobutton(label_frame,
                         text="Male",
                         variable=var)
radio_male.grid(row=8, column=0)

var2 = IntVar()
radio_female = Radiobutton(label_frame,
                         text="Female",
                         variable=var2)
radio_female.grid(row=8, column=1)

# 5 chi qator ------------------------------------------------
address_label = Label(label_frame,
                       text="Address",
                       font=("Calibri", 15))
address_label.grid(row=9, column=0)
address_entry = Entry(label_frame, width=70)
address_entry.grid(row=10, column=0, ipady=7, columnspan=2, sticky="news")

# 5 chi qator ------------------------------------------------
combo_country = Combobox(label_frame,
                         values=["Uzbekistan", "Turkiye",
                                 "USA", "Phalastine",
                                 "Russian", "China"])
combo_country.grid(row=11, column=0, ipadx=30, ipady=7)

code_entry = Entry(label_frame, width=30)
code_entry.grid(row=11, column=1, ipady=7)

button = Button(label_frame,
                text="Submit",
                font=("Calibri", 15, "bold"),
                bg="#826BFB",
                fg="white",
                command=register_func)
button.grid(row=12, column=0, columnspan=2, sticky="news")


for widget in label_frame.winfo_children():
    widget.grid_configure(padx=8, pady=5)

windows.mainloop()