""" Making a basic Text App """
""" TKinter """
""" By: Dhruv """

# Importing module
# TKinter
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Style

""" Variables """
# region Variables
# Color of the Sidebar
sidebar_color = "#21252B"
# Color of the topbar
topbar_color = "#333842"
# Color of the text field
textfield_color = "#333842"

opened_file_address = ""
# endregion

""" Functions """
# region Functions

#  Prompts the File Explorer to select a text file (*.txt)
def open_fileopener():
    opened_file_address = filedialog.askopenfilename(
        initialdir="C:\\Users\\vivek\\OneDrive\\Desktop\\DHRUV\\Docs",
        title="Open a Text File",
        filetypes=(("Text files", "*.txt"), ("All Files", ("*.*"))),
    )
    # Opens the selected text file and inserts the text in the text field.
    def open_file():
        selected_file = open(opened_file_address, "r")
        file_text = selected_file.read()
        text_field.insert(END, file_text)
        selected_file.close()

    print(f"Opened {opened_file_address}")
    if opened_file_address != None:
        open_file()


def display_file_address():
    sidebar_file_display = Label(sidebar_frame, text=opened_file_address)
    sidebar_file_display.pack()


# Close out the application.
# ROOT.quit()
def exit():
    print("Quit")
    ROOT.quit()


# endregion

# Creating instance
ROOT = Tk()

# Creating a Style Object
STYLE = Style()

# Creating a Main Menu
MAIN_MENU = Menu(ROOT)

# Config the Menu in ROOT
ROOT.config(menu=MAIN_MENU)

# Configuring button style
STYLE.configure(
    "TButton", font=("Andromeda", 12, "bold", "underline"), foreground="blue"
)

# Setting the Geometry of the Window
# Default Size: 600 x 400

ROOT.geometry("600x400")

# Setting minsize and maxsize
# minsize = 90 x 180

ROOT.minsize(180, 90)

# Setting the title of the window.
ROOT.title("TK Text Editor")

# Ading an icon
ROOT.iconbitmap("win-icon.ico")

# configuring the base color of the applicaiton
# color => #333842
ROOT.configure(bg="#333842")

# Creating a Frame
sidebar_frame = Frame(ROOT, width=600, bg=sidebar_color, relief=SUNKEN, borderwidth=4)
# Stretching the sidebar on Y-Axis
sidebar_frame.pack(side=LEFT, fill="y")

# Title bar
titlebar_frame = Frame(ROOT, bg=sidebar_color, relief=FLAT)
titlebar_frame.pack(side=TOP, fill="x")

# Topbar
topbar_frame = Frame(ROOT, bg=topbar_color, relief=FLAT)
# stretching the topbar on the X-Axis
topbar_frame.pack(side=TOP, fill="x")

text_field_frame = Frame(ROOT)
text_field_frame.pack()

# Adding a Menu panel
file_menu = Menu(MAIN_MENU)
MAIN_MENU.add_cascade(label="File", menu=file_menu)
# General File commands
    # Open a file => open_fileopener()
    # Exit => exit()
file_menu.add_command(label="Open a file", command=open_fileopener)
file_menu.add_command(label="Exit", command=exit)

# Adding a label
sidebar_label = Label(sidebar_frame, text="Sidebar", relief=RAISED, width=20)
sidebar_label.pack(pady=2)

title_label = Label(
    titlebar_frame, text="TK Text Editor", font=("abel", "12", "bold"), relief=RAISED
)
title_label.pack(pady=6, anchor=CENTER)

# Create a button to open file opener
openfile_button = Button(
    topbar_frame,
    height=1,
    text="Open a file",
    command=lambda: [open_fileopener(), display_file_address()],
)
openfile_button.grid(row=0, column=0, padx=8, pady=2)

# Close window on click.
# Terminates the program.
close_window_button = Button(topbar_frame, height=1, text="Close", command=exit)
close_window_button.grid(row=0, column=1, padx=6, pady=2)

# Text field.
# Takes user input.
text_field = Text(
    text_field_frame, font=("fira code", "18"), bg=textfield_color, fg="white"
)
text_field.pack(fill="both")

# Running mainloop
ROOT.mainloop()
