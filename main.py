""" D-Pad | Text Editor """
""" TKinter """
""" By: Dhruv and ygz213"""


from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import colorchooser
import webbrowser
import os
from message import alert

font_color = "#C5D4DD"
# Color of the Sidebar
sidebar_color = "#1E272C"
# Color of the topbar
topbar_color = "#333842"
# Color of the text field
textfield_color = "#333842"

default_bg = "#445660"

# Default font of the text field
text_font = "Consolas"

text_field_content = ""

selected_text = ""

opened_file_address = ""

# List of all available fonts
available_fonts = ("Abel", "Andromeda", "Consolas", "Consequences", "Helvetica")

# Constants
# -anchor and -sticky
N = "n"
S = "s"
W = "w"
E = "e"
NW = "nw"
SW = "sw"
NE = "ne"
SE = "se"
NS = "ns"
EW = "ew"
NSEW = "nsew"
CENTER = "center"

# -fill
NONE = "none"
X = "x"
Y = "y"
BOTH = "both"

# -side
LEFT = "left"
TOP = "top"
RIGHT = "right"
BOTTOM = "bottom"

# -relief
RAISED = "raised"
SUNKEN = "sunken"
FLAT = "flat"
RIDGE = "ridge"
GROOVE = "groove"
SOLID = "solid"

# endregion

""" Functions """
# region Functions

#  Prompts the File Explorer to select a text file (*.txt)


def new_file():
    ROOT.title("Untitled | D-Pad")
    text_field.delete(1.0, "end")


def open_fileopener():
    global opened_file_address
    opened_file_address = filedialog.askopenfilename(
        initialdir="/",
        title="Open a Text File",
        filetypes=(("Text files", "*.txt"), ("All Files", ("*.*"))),
    )

    # Opens the selected text file and inserts the text in the text field.
    def open_file():
        try:
            with open(opened_file_address, "r") as selected_file:
                file_text = selected_file.read()
                text_field.insert("end", file_text)
        except Exception:
            print("Oops! There was a problem opening that file")
            alert("Oops! There was a problem opening that file")

    if opened_file_address != "":
        global file_name
        file_name = os.path.basename(opened_file_address)
        open_file()
        if ".txt" in file_name:
            ROOT.title(f"{file_name} | D-Pad")
            print(f"Opened {file_name} [{opened_file_address}]")
        else:
            print("No text file selected")


# Saves the file in the opened file address
def save_file():
    global opened_file_address

    if opened_file_address == "":
        save_file_as()
    else:
        with open(opened_file_address, "w") as selected_file:
            selected_file.write(text_field.get(1.0, "end"))


def save_file_as():
    global opened_file_address

    file = filedialog.asksaveasfile(
        initialdir="/",
        title="Save file as...",
        filetypes=(("Text files", "*.txt"), ("All Files", ("*.*"))),
    )

    opened_file_address = file.name
    file_name = os.path.basename(opened_file_address)
    if ".txt" in file_name:
        ROOT.title(f"{file_name} | D-Pad")
        print(f"Opened {file_name} [{opened_file_address}]")
    else:
        print("No text file selected")

    with open(opened_file_address, "w") as selected_file:
        selected_file.write(text_field.get(1.0, "end"))

    display_file_address()


def display_file_address():
    if opened_file_address != "":
        global sidebar_file_address_display
        sidebar_file_address_display = Label(
            sidebar_frame, text=opened_file_address, wraplength=120
        )
        sidebar_file_address_display.pack(pady=20)


def clear_sidebar():
    for labels in sidebar_frame.children.values():
        labels.pack_forget()
    sidebar_label = Label(
        sidebar_frame,
        text="Sidebar",
        relief="flat",
        width=20,
        bg=sidebar_color,
        fg="white",
    )
    sidebar_label.pack(pady=2)

    sidebar_collapse_button = Button(sidebar_frame, text="<<", command=collapse_sidebar)
    sidebar_collapse_button.pack(anchor="sw")


# Close out the application.
# ROOT.quit()


def exit():
    print("Quit")
    ROOT.destroy()


# Clears the text field
def clear():
    text_field.delete(1.0, "end")


def open_settings():
    # Window Options
    settings_window = Toplevel()
    settings_window.title("D-Pad Settings")

    settings_window.minsize(200, 150)
    settings_window.minsize(250, 200)

    # Font selection
    font_label = Label(settings_window, text="Select a Font: ")
    font_label.pack(side="left", anchor=W)
    font_button = Button(settings_window, text="Font...", command=open_font_selector)
    font_button.pack(side="left", anchor=W)

    font_size_label = Label(settings_window, text="Set Font Size: ")
    font_size_label.pack(side="left", anchor=W)

    selected_font_size = StringVar()
    font_size_entry = Entry(settings_window, textvariable=selected_font_size)
    font_size_entry.pack(side="left", anchor=W)

    def apply_font_size():
        text_field.config(font=(text_font, selected_font_size.get()))

    apply_font_button = Button(settings_window, text="Okay", command=apply_font_size)
    apply_font_button.pack(side=BOTTOM, anchor=SE)


""" Text Operations """

# Bold Format Option


def text_bold():
    # Un-bold the text
    def remove_bold():
        text_field.tag_remove("bold", "sel.first", "sel.last")

    # Make the text bold.
    def add_bold():
        text_field.tag_add("bold", "sel.first", "sel.last")

    bold_font = font.Font(text_field, text_field.cget("font"))
    bold_font.configure(weight="bold")

    text_field.tag_configure("bold", font=bold_font)

    text_tags = text_field.tag_names("sel.first")

    # Check if the 'BOLD' tag is there
    if "bold" in text_tags:
        remove_bold()
    else:
        add_bold()


def italicize():
    def remove_italics():
        text_field.tag_remove("italic", "sel.first", "sel.last")

    def add_italics():
        text_field.tag_add("italic", "sel.first", "sel.last")

    italic_font = font.Font(text_field, text_field.cget("font"))
    italic_font.configure(slant="italic")

    text_field.tag_configure("italic", font=italic_font)

    text_tags = text_field.tag_names("sel.first")

    if "italic" in text_tags:
        remove_italics()
    else:
        add_italics()


def underline_text():
    def add_underline():
        text_field.tag_add("underline", "sel.first", "sel.last")

    def remove_underline():
        text_field.tag_remove("underline", "sel.first", "sel.last")

    under_text = font.Font(text_field, text_field.cget("font"))
    under_text.configure(underline=True)

    text_field.tag_configure("underline", font=under_text)

    text_tags = text_field.tag_names("sel.first")

    if "underline" in text_tags:
        remove_underline()
    else:
        add_underline()


def highlight_text():
    highlight_color = "#FFFF00"

    def add_highlight():
        text_field.tag_add("highlight", "sel.first", "sel.last")

    def remove_highlight():
        text_field.tag_remove("highlight", "sel.first", "sel.last")

    highlighted_text = font.Font(text_field, text_field.cget("font"))

    text_field.tag_configure("highlight", font=highlighted_text)
    text_field.tag_config("highlight", background=highlight_color, foreground="white")
    text_tags = text_field.tag_names("sel.first")

    if "highlight" in text_tags:
        remove_highlight()
    else:
        add_highlight()


# Cut
# Copy
# Paste


def cut_text():
    if text_field.selection_get():
        selected_text = text_field.selection_get()
        ROOT.clipboard_clear()
        ROOT.clipboard_append(selected_text)
        text_field.delete("sel.first", "sel.last")


# copy selected text
def copy_text():
    if text_field.selection_get():
        selected_text = text_field.selection_get()
        ROOT.clipboard_clear()
        ROOT.clipboard_append(selected_text)


# paste text
def paste_text():
    pasted_text = ROOT.clipboard_get()
    text_position = text_field.index(INSERT)
    text_field.insert(text_position, pasted_text)


def change_font_color():
    color_select = colorchooser.askcolor()
    text_field.config(fg=color_select[1])


# Open the repository page
# Link: [https://github.com/iDCoded/D-Pad]


def open_github_repo():
    repo_url = "https://github.com/iDCoded/D-Pad"
    webbrowser.open_new_tab(repo_url)


# Open a Toplevel window for font selection.
def open_font_selector():
    global text_font

    def select_font():
        text_field.config(font=(selected_font.get()))

    font_window = Toplevel()
    font_window.title("Font")
    # Set the Geometry of the window.
    font_window.geometry("200x150")
    font_window.minsize(200, 150)
    font_window.maxsize(250, 200)

    selected_font = StringVar(font_window)
    # Set the first options as the initial menu for the dropdown.
    selected_font.set(available_fonts[0])
    fonts_label = Label(font_window, text="Select a Font: ")
    fonts_label.pack()
    # Selector for fonts
    # font_selection_drop = OptionMenu(font_window, selected_font, *available_fonts)
    # font_selection_drop.pack()

    fontbox = OptionMenu(
        font_window, selected_font, *font.families(), command=select_font
    )
    fontbox.pack()

    text_font = selected_font.get()

    final_button = Button(font_window, text="Ok", command=select_font)
    final_button.pack(side=RIGHT, anchor=SE)


# Right Click Popups

# Sidebar RC
def sidebar_popup(e):
    sidebar_right_click.tk_popup(e.x_root, e.y_root)


# Text Field RC
def text_field_popup(e):
    text_field_right_click.tk_popup(e.x_root, e.y_root)


def collapse_sidebar():
    # print(sidebar_pack_info)
    sidebar_frame.pack_forget()


def show_sidebar():
    sidebar_frame.pack(fill=Y, side="left")

    titlebar_frame.pack_forget()
    titlebar_frame.pack(side="top", fill="x")

    topbar_frame.pack_forget()
    topbar_frame.pack(side="top", fill=X)

    text_field_frame.pack_forget()
    text_field_frame.pack(fill="both")


# endregion
if __name__ == "__main__":

    # Creating instance
    ROOT = Tk()

    # Creating a Main Menu
    # Save, Open, Exit
    MAIN_MENU = Menu(ROOT)

    # Creating Edit menu
    # Text editing options : Cut, Copy Paste.
    EDIT_MENU = Menu(ROOT)
    # Misc menu
    # Link to my GitHub Repo
    MISC_MENU = Menu(ROOT)

    # View Menu
    VIEW_MENU = Menu(ROOT)

    # Config the Menu in ROOT
    ROOT.config(menu=MAIN_MENU)

    # Setting the Geometry of the Window
    # Default Size: 600 x 400

    ROOT.geometry("600x400")

    # Setting minsize and maxsize
    # minsize = 90 x 180

    ROOT.minsize(180, 90)

    # Setting the title of the window.
    ROOT.title(" D-Pad")

    # Runs program fullscreen
    ROOT.state("zoomed")

    # Adding an icon
    ROOT.iconbitmap("win-icon.ico")

    # configuring the base color of the application
    # color => #333842
    ROOT.configure(bg=default_bg)

    # Creating a Frame
    sidebar_frame = Frame(
        ROOT, width=2400, bg=sidebar_color, relief="sunken", borderwidth=4
    )
    # Stretching the sidebar on Y-Axis
    sidebar_frame.pack(side="left", fill="both")

    # Title bar
    titlebar_frame = Frame(ROOT, bg=sidebar_color, relief="flat")
    titlebar_frame.pack(side="top", fill="x")

    # Topbar
    topbar_frame = Frame(ROOT, bg=topbar_color, relief="flat")
    # stretching the topbar on the X-Axis
    topbar_frame.pack(side="top", fill="x")

    text_field_frame = Frame(ROOT)
    text_field_frame.pack(fill="both")

    # Text field.
    # Takes user input.
    text_field = Text(
        text_field_frame,
        font=(text_font, "18"),
        bg=textfield_color,
        fg="white",
        undo="true",
    )
    text_field.pack(fill="both")

    # Adding a Menu panel
    file_menu = Menu(MAIN_MENU, tearoff=False)
    MAIN_MENU.add_cascade(label="File", menu=file_menu)
    # General File commands
    # Open a file => open_fileopener()
    # Savve => save_file()
    # Exit => exit()
    file_menu.add_command(label="New File", command=new_file, accelerator="Ctrl + N")
    file_menu.add_command(
        label="Open a file",
        command=lambda: [open_fileopener(), display_file_address()],
        accelerator="Ctrl + O",
    )
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Save As..", command=save_file_as)
    file_menu.add_separator()
    file_menu.add_command(
        label="Settings...", accelerator="Ctrl + ,", command=open_settings
    )
    file_menu.add_separator()
    file_menu.add_command(label="Save & Exit", command=lambda: [save_file(), exit()])
    file_menu.add_command(label="Exit", command=exit, accelerator="Ctrl+W")

    # Edit Menu
    edit_menu = Menu(EDIT_MENU, tearoff=False)
    MAIN_MENU.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl + X")
    edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl + C")
    edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl + V")
    edit_menu.add_separator()
    edit_menu.add_command(label="Font..", command=open_font_selector)
    edit_menu.add_command(label="Color", command=change_font_color)

    view_menu = Menu(VIEW_MENU, tearoff=False)
    MAIN_MENU.add_cascade(label="View", menu=view_menu)
    view_menu.add_command(label="Show Sidebar", command=show_sidebar)

    # Misc menu
    misc_menu = Menu(MISC_MENU, tearoff=False)
    MAIN_MENU.add_cascade(label="Misc.", menu=misc_menu)

    # Link : {'https://github.com/iDCoded/D-Pad'}
    misc_menu.add_command(label="GitHub Repo", command=open_github_repo)

    # Right Click

    # Sidebar
    sidebar_right_click = Menu(ROOT, tearoff=False)
    sidebar_right_click.add_command(label="Collapse Sidebar", command=collapse_sidebar)
    sidebar_right_click.add_command(label="Clear", command=clear_sidebar)

    # Text field
    text_field_right_click = Menu(ROOT, tearoff=False)
    text_field_right_click.add_command(label="Clear", command=clear)

    # binding button-3 (right-click)
    sidebar_frame.bind("<Button-3>", sidebar_popup)
    text_field.bind("<Button-3>", text_field_popup)

    # Key Bindings

    # [CTRL-W] => Exit the application.
    ROOT.bind("<Control-w>", lambda x: exit())

    # [CTRL-O] => Open a file.
    ROOT.bind("<Control-o>", lambda x: [open_fileopener(), display_file_address()])

    # Adding a label
    sidebar_label = Label(
        sidebar_frame,
        text="Sidebar",
        relief="flat",
        width=20,
        bg=sidebar_color,
        fg="white",
    )
    sidebar_label.pack(pady=2)

    title_label = Label(
        titlebar_frame,
        text="D-Pad | Text Editor",
        font=("abel", "12", "bold"),
        relief="flat",
        background=sidebar_color,
        foreground=font_color,
    )
    title_label.pack(pady=6, anchor="center", fill="x")

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
    clear_button = Button(topbar_frame, height=1, text="Clear", command=clear)
    clear_button.grid(row=0, column=1, padx=6, pady=2)

    # Text Formatting
    # Bold & Italics

    bold_button = Button(topbar_frame, height=1, text="Bold", command=text_bold)
    bold_button.grid(row=0, column=2)

    italics_button = Button(topbar_frame, height=1, text="Italics", command=italicize)
    italics_button.grid(row=0, column=3)

    underline_button = Button(
        topbar_frame, height=1, text="Underline", command=underline_text
    )
    underline_button.grid(row=0, column=4)

    highlight_button = Button(topbar_frame, text="Highlight", command=highlight_text)
    highlight_button.grid(row=0, column=5)

    sidebar_collapse_button = Button(sidebar_frame, text="<<", command=collapse_sidebar)
    sidebar_collapse_button.pack(anchor="sw")

    # Store the input into the
    # text_field
    text_field_content = StringVar()
    text_field_content = text_field.get(1.0, "end")

    # Running mainloop
    ROOT.mainloop()
