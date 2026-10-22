from tkinter import *

root = Tk()

# 1. Create the main menu bar
menu = Menu(root)
root.config(menu=menu)

# 2. Create a dropdown menu
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

# 3. Add options inside the dropdown
filemenu.add_command(label="New")
filemenu.add_command(label="Exit", command=root.quit)

# 4. Run the window
root.mainloop()