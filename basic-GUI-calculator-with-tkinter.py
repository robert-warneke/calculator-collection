import tkinter as tk
from tkinter import messagebox
from asteval import Interpreter

def create_button(root, text, cmd, row, col, bg='#3E4042', fg='#FFFFFF', h=2, w=4, f=('Helvetica', 20), span=1):
    button = tk.Button(root, text=text, height=h, width=w, bg=bg, fg=fg, font=f, command=cmd)
    button.grid(row=row, column=col, padx=5, pady=5, columnspan=span)

# Create a interpreter for safe evaluation of mathematical expressions
aeval = Interpreter()

# Create main window
root = tk.Tk()
root.title('Basic Calculator')
root.configure(bg='#333')
root.resizable(False, False)

# Entry field to show calculations
entry = tk.Entry(root, width=14, borderwidth=5, bg='#333', fg='#e8e8e8', font=('Helvetica', 32))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_equal():
    try:
        value = aeval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, value)
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression")
        entry.delete(0, tk.END)

def button_clear():
    entry.delete(0, tk.END)

def button_backspace():
    entry.delete(len(entry.get())-1, tk.END)

# Create clear and backspace buttons
create_button(root, 'Clear', button_clear, 1, 0, '#f04747', h=2, w=9, span=2)
create_button(root, '<-', button_backspace, 1, 2, '#f04747', h=2, w=4, span=1)

# Create number buttons in calculator-style order
numbers = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['.', '0', None]]
for i in range(4):
    for j in range(3):
        if numbers[i][j]:
            create_button(root, numbers[i][j], lambda n=numbers[i][j]: button_click(n), i+2, j)

# Create operator buttons with a different color
operators = ['/', '*', '+', '-']
for i, operator in enumerate(operators):
    create_button(root, operator, lambda o=operator: button_click(o), i+1, 3, '#7289DA')

# Create equal button
create_button(root, '=', button_equal, 5, 2, '#43b581', h=2, w=9, span=2)

# Run the GUI
root.mainloop()
