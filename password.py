from tkinter import *
import string
import random

def generate_password():
    password = ''
    lower_letters = list(string.ascii_lowercase)
    upper_letters = list(string.ascii_uppercase)
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    all_chars = lower_letters + upper_letters + digits
    length = int(length_entry.get())
    
    for _ in range(length):
        password += str(random.choice(all_chars))
        
    password_output.delete(0, END)
    password_output.insert(0, password)

def reset_fields():
    username_entry.delete(0, END)
    length_entry.delete(0, END)
    password_output.delete(0, END)
    final_username_label.config(text="", bg="#d3f7bf")
    final_password_label.config(text="", bg="#d3f7bf")

def accept_credentials():
    username_text = username_entry.get() + " ! Please remember your password: "
    final_username_label.config(text=username_text,
                                font=("Arial", 20, "bold"),
                                fg="blue",
                                bg="#d3f7bf")
    final_password_label.config(text=password_output.get(),
                                font=("Arial", 20, "bold"),
                                bg="#d3f7bf")

window = Tk()
window.geometry("900x900")
window.config(bg="#d3f7bf")
window.title("Password Generator")

title_label = Label(window,
                    text="Secure Password Generator",
                    font=("Arial", 40, "bold"),
                    fg="black",
                    bg="#d3f7bf")
title_label.place(x=250, y=10)

username_label = Label(window,
                       text="Enter Username:",
                       font=("Arial", 20, "bold"),
                       fg="red",
                       bg="#d3f7bf")
username_label.place(x=100, y=150)

username_entry = Entry(window,
                       font=("Arial", 20),
                       fg="black",
                       bg="white")
username_entry.place(x=350, y=150)

length_label = Label(window,
                     text="Enter Password Length:",
                     font=("Arial", 20, "bold"),
                     fg="red",
                     bg="#d3f7bf")
length_label.place(x=100, y=250)

length_entry = Entry(window,
                     font=("Arial", 20),
                     fg="black",
                     bg="white")
length_entry.place(x=450, y=250)

password_label = Label(window,
                       text="Generated Password:",
                       font=("Arial", 20, "bold"),
                       fg="green",
                       bg="#d3f7bf")
password_label.place(x=100, y=350)

password_output = Entry(window,
                        font=("Arial", 20, "bold"),
                        fg="black",
                        bg="lightyellow")
password_output.place(x=450, y=350)

generate_button = Button(window,
                         text="GENERATE PASSWORD",
                         font=("Arial", 20),
                         bg="blue",
                         fg="white",
                         bd=2,
                         command=generate_password)
generate_button.place(x=350, y=450)

accept_button = Button(window,
                       text="ACCEPT",
                       font=("Arial", 17),
                       bg="yellow",
                       fg="black",
                       bd=4,
                       command=accept_credentials)
accept_button.place(x=300, y=550)

reset_button = Button(window,
                      text="RESET",
                      font=("Arial", 17),
                      bg="yellow",
                      fg="black",
                      bd=4,
                      command=reset_fields)
reset_button.place(x=550, y=550)

final_username_label = Label(window, bg="#d3f7bf")
final_username_label.place(x=100, y=650)

final_password_label = Label(window, bg="#d3f7bf")
final_password_label.place(x=100, y=700)

window.mainloop()
