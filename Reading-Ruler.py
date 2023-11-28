import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askinteger, askfloat

def on_close(event):
    root.destroy()

def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def do_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

def change_color():
    color_code = askcolor(title="Choose color")
    if color_code[1] is not None:
        root.configure(bg=color_code[1])

def change_transparency():
    transparency = askfloat("Transparency", "Enter a value between 0 and 1:", minvalue=0, maxvalue=1,initialvalue=root.attributes('-alpha'))
    if transparency is not None:
        root.attributes('-alpha', transparency)

def change_size():
    width = askinteger("Width", "Enter the width of the window:",initialvalue=root.winfo_width())
    height = askinteger("Height", "Enter the height of the window:",initialvalue=root.winfo_height())
    if width is not None and height is not None:
        root.geometry(f"{width}x{height}")

root = tk.Tk()
root.geometry('300x100')  # Size of the rectangle
root.configure(bg='#77dd77')  # Pastel green background color
root.attributes('-alpha', 0.5)  # Translucency level between 0 (transparent) and 1 (opaque)
root.attributes('-topmost', 1)  # Makes the window stay on top of others
root.overrideredirect(1)  # Removes the title bar

# Create a context menu
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Background color", command=change_color)
menu.add_command(label="Transparency", command=change_transparency)
menu.add_command(label="Window size", command=change_size)

# Bind the context menu to the window
def show_menu(event):
    menu.post(event.x_root, event.y_root)
root.bind("<Button-3>", show_menu)

# Listen for double click on the window
root.bind('<Double-1>', on_close)

# Make the window resizable
root.bind("<ButtonPress-1>", start_move)
root.bind("<ButtonRelease-1>", stop_move)
root.bind("<B1-Motion>", do_move)

root.mainloop()
