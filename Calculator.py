import tkinter as tk

# Function to perform the calculation
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to delete the last character in the entry field
def delete_last():
    entry.delete(len(entry.get()) - 1)

# Function to calculate the percentage
def calculate_percentage():
    try:
        expression = entry.get()
        number = eval(expression)
        result = number / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Mohsin's Calculator")

# Create an entry field to display the input and output 
entry = tk.Entry(window, width=50, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operators
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("00", 4, 2), ("+", 4, 3)
]

for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, width=10, command=lambda text=button_text: entry.insert(tk.END, text))
    button.grid(row=row, column=column)

# Create a button for clearing the entry field
clear_button = tk.Button(window, text="C", width=10,bg="green", command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=5, column=0)


# Create a button for deleting the last character
delete_button = tk.Button(window, text="DEL", width=10,bg="red", command=delete_last)
delete_button.grid(row=5, column=2)

# Create a button for calculating the result
equal_button = tk.Button(window, text="=", width=10 ,bg="green", command=calculate)
equal_button.grid(row=5, column=3)

# Create a button for calculating the percentage
percentage_button = tk.Button(window, text="%", width=10, command=calculate_percentage)
percentage_button.grid(row=5, column=1)

# Start the main event loop
window.mainloop()
