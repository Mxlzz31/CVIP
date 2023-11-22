import tkinter as tk

def on_click(value):
    current = str(entry.get())
    new_value = str(value)

    if current == "0":
        entry.delete(0, tk.END)
        entry.insert(0, new_value)
    else:
        entry.insert(tk.END, new_value)

def clear_entry():
    entry.delete(0, tk.END)
    entry.insert(0, "0")

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for display
entry = tk.Entry(root, width=16, font=('Arial', 20), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place buttons
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, width=4, height=2, command=lambda b=button: on_click(b) if b != '=' else calculate() if b != 'C' else clear_entry()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()
