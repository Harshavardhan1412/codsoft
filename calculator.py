import tkinter as tk
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def clear():
    entry.delete(0, tk.END)
def add_display(char):
    entry.insert(tk.END, char)
root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, width=20, font=("times new roman", 14), bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+']
r = 1
c = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=10, height=2, command=calculate).grid(row=r, column=c, padx=5, pady=5)
    elif button == 'C':
        tk.Button(root, text=button, width=10, height=2, command=clear).grid(row=r, column=c, padx=5, pady=5)
    else:
        tk.Button(root, text=button, width=10, height=2, command=lambda char=button: add_display(char)).grid(row=r, column=c, padx=5, pady=5)
    c += 1
    if c > 3:
        c = 0
        r += 1
root.mainloop()
