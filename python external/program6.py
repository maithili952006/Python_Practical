

import tkinter as tk

# Create window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

# Create label
label = tk.Label(root, text="Welcome to Python")
label.pack()

# Create text box
entry = tk.Entry(root)
entry.pack()

# Function for button click
def submit():
    name = entry.get()
    result.config(text="Hello " + name)

# Create button
button = tk.Button(root, text="Submit", command=submit)
button.pack()

# Display result
result = tk.Label(root, text="")
result.pack()

# Run application
root.mainloop()