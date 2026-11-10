import tkinter as tk

root = tk.Tk()
root.title("My 1st GUI")
root.geometry("300x200")

label = tk.Label(root,text="Welcome to python")
label.pack()

entry = tk.Entry(root)
entry.pack()

def submit():
    name = entry.get()
    result.config(text="Hello" + name)
    
button = tk.Button(root, text='Submit', command = submit)    
button.pack()

result = tk.Label(root,text="")
result.pack()

root.mainloop()