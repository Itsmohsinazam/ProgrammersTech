import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    if length <= 0:
        raise ValueError("Password length must be greater than 0")
    
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    try:
        length = int(entry_length.get())
        use_uppercase = var_uppercase.get()
        use_lowercase = var_lowercase.get()
        use_digits = var_digits.get()
        use_special = var_special.get()
        
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Length input
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Checkbuttons for character types
var_uppercase = tk.BooleanVar(value=True)
var_lowercase = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=var_uppercase).grid(row=1, column=0, columnspan=2, sticky='w', padx=10)
tk.Checkbutton(root, text="Include Lowercase", variable=var_lowercase).grid(row=2, column=0, columnspan=2, sticky='w', padx=10)
tk.Checkbutton(root, text="Include Digits", variable=var_digits).grid(row=3, column=0, columnspan=2, sticky='w', padx=10)
tk.Checkbutton(root, text="Include Special Characters", variable=var_special).grid(row=4, column=0, columnspan=2, sticky='w', padx=10)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password_gui).grid(row=5, column=0, columnspan=2, pady=10)

# Entry to display the generated password
entry_password = tk.Entry(root, width=50)
entry_password.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()