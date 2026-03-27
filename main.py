import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_slider.get()
    
    characters = ""
    if var_uppercase.get():
        characters += string.ascii_uppercase
    if var_lowercase.get():
        characters += string.ascii_lowercase
    if var_numbers.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation
        
    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return
        
    password = "".join(random.choice(characters) for _ in range(length))
    
    # Enable the entry, insert the password, and set it to readonly again
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("450x650")
root.configure(padx=30, pady=30)

# Styling
font_title = ("Segoe UI", 18, "bold")
font_normal = ("Segoe UI", 11)

# Title
title_label = tk.Label(root, text="Password Generator", font=font_title)
title_label.pack(pady=(0, 20))

# Password Display Frame
display_frame = tk.Frame(root)
display_frame.pack(fill="x", pady=(0, 20))

password_entry = tk.Entry(display_frame, font=("Consolas", 14), justify="center", state="readonly")
password_entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 10))

# Copy Button
copy_btn = tk.Button(display_frame, text="Copy", font=font_normal, command=copy_to_clipboard, width=6)
copy_btn.pack(side="right", ipady=5)

# Length
length_frame = tk.Frame(root)
length_frame.pack(fill="x", pady=(0, 20))
length_label = tk.Label(length_frame, text="Password Length:", font=font_normal)
length_label.pack(anchor="w", pady=(0, 5))
length_slider = tk.Scale(length_frame, from_=4, to=64, orient="horizontal", font=font_normal)
length_slider.set(16)
length_slider.pack(fill="x")

# Options
options_frame = tk.Frame(root)
options_frame.pack(fill="x", pady=(0, 20))

var_uppercase = tk.BooleanVar(value=True)
var_lowercase = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

chk_upper = tk.Checkbutton(options_frame, text="Include Uppercase Letters (A-Z)", variable=var_uppercase, font=font_normal)
chk_upper.pack(anchor="w", pady=2)
chk_lower = tk.Checkbutton(options_frame, text="Include Lowercase Letters (a-z)", variable=var_lowercase, font=font_normal)
chk_lower.pack(anchor="w", pady=2)
chk_numbers = tk.Checkbutton(options_frame, text="Include Numbers (0-9)", variable=var_numbers, font=font_normal)
chk_numbers.pack(anchor="w", pady=2)
chk_symbols = tk.Checkbutton(options_frame, text="Include Symbols (!@#$)", variable=var_symbols, font=font_normal)
chk_symbols.pack(anchor="w", pady=2)

# Generate Button
generate_btn = tk.Button(root, text="GENERATE PASSWORD", font=("Segoe UI", 12, "bold"), bg="#0078D7", fg="white", activebackground="#005A9E", activeforeground="white", command=generate_password, relief="flat")
generate_btn.pack(fill="x", ipady=12, pady=(10, 0))

# Footer Name
footer_label = tk.Label(root, text="BUILT BY PIYUSH GUPTA", font=("Segoe UI", 11, "bold"), fg="#0000FF")
footer_label.pack(pady=(25, 0))

# Generate initial password
generate_password()

root.mainloop()
