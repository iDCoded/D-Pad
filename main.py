""" D-Pad | Text Editor """
""" TKinter """
""" By: Dhruv """

# Importing module
# TKinter
from tkinter import *
from tkinter import font
from tkinter import filedialog

# from tkinter.ttk import Style
import webbrowser
import os

""" Variables """
# region Variables

""" Color Theme """
font_color = "#C5D4DD"
# Color of the Sidebar
sidebar_color = "#1E272C"
# Color of the topbar
topbar_color = "#333842"
# Color of the text field
textfield_color = "#333842"

default_bg = "#445660"

# Default font of the text field
global text_font
text_font = "Consolas"

global text_field_content
text_field_content = ""

global selected_text
selected_text = ""

opened_file_address = ""

# List of all available fonts
global available_fonts
available_fonts = ("Abel", "Andromeda", "Consolas", "Consequences", "Helvetica")
# {"Abel", "Andromeda", "Consolas", "Consequences", "Helvetica"}

# endregion

""" Functions """
# region Functions
def check_text_file():
    if ".txt" in file_name:
        return True
    else:
        return False


#  Prompts the File Explorer to select a text file (*.txt)
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
                text_field.insert(END, file_text)
        except Exception:
            print("Oops! There was a problem opening that file")

    if opened_file_address != "":
        global file_name
        file_name = os.path.basename(opened_file_address)
        open_file()
        if ".txt" in file_name:
            ROOT.title(f"{file_name} | D-Pad")
            print(f"Opened {opened_file_address} [{file_name}]")
        else:
            print("No text file selected")


# Saves the file in the opened file address
def save_file():
    global opened_file_address
    opened_file_address = filedialog.askopenfilename(
        initialdir="/",
        title="Save file as...",
        filetypes=(("Text files", "*.txt"), ("All Files", ("*.*"))),
    )
    if opened_file_address != "":
        with open(opened_file_address, "w") as selected_file:
            selected_file.write(text_field.get(1.0, END))


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
        relief=FLAT,
        width=20,
        bg=sidebar_color,
        fg="white",
    )
    sidebar_label.pack(pady=2)


# Close out the application.
# ROOT.quit()
def exit():
    print("Quit")
    ROOT.destroy()


# Clears the text field
def clear():
    text_field.delete(1.0, END)


""" Text Operations """

# Cut
# Copy
# Paste

# cut selected text
def cut_text():
    if text_field.selection_get():
        selected_text = text_field.selection_get()
        ROOT.clipboard_clear()
        ROOT.clipboard_append(selected_text)
        text_field.delete(SEL_FIRST, SEL_LAST)


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


# Bold Format Option
def text_bold():
    # Un-bold the text
    def remove_bold():
        text_field.tag_remove("bold", SEL_FIRST, SEL_LAST)

    # Make the text bold.
    def add_bold():
        text_field.tag_add("bold", SEL_FIRST, SEL_LAST)

    bold_font = font.Font(text_field, text_field.cget("font"))
    bold_font.configure(weight="bold")

    text_field.tag_configure("bold", font=bold_font)

    text_tags = text_field.tag_names(SEL_FIRST)

    # Check if the 'BOLD' tag is there
    if "bold" in text_tags:
        remove_bold()
    else:
        add_bold()


def italicize():
    def remove_italics():
        text_field.tag_remove("italic", SEL_FIRST, SEL_LAST)

    def add_italics():
        text_field.tag_add("italic", SEL_FIRST, SEL_LAST)

    italic_font = font.Font(text_field, text_field.cget("font"))
    italic_font.configure(slant="italic")

    text_field.tag_configure("italic", font=italic_font)

    text_tags = text_field.tag_names(SEL_FIRST)

    if "italic" in text_tags:
        remove_italics()
    else:
        add_italics()


def underline_text():
    def add_underline():
        text_field.tag_add("underline", SEL_FIRST, SEL_LAST)

    def remove_underline():
        text_field.tag_remove("underline", SEL_FIRST, SEL_LAST)

    under_text = font.Font(text_field, text_field.cget("font"))
    under_text.configure(underline=True)

    text_field.tag_configure("underline", font=under_text)

    text_tags = text_field.tag_names(SEL_FIRST)

    if "underline" in text_tags:
        remove_underline()
    else:
        add_underline()


# Open the repository page
# Link: [https://github.com/iDCoded/D-Pad]
def open_github_repo():
    repo_url = "https://github.com/iDCoded/D-Pad"
    webbrowser.open_new_tab(repo_url)


# Open a Toplevel window for font selection.
def open_font_selector():
    global text_font

    def select_font():
        text_font = selected_font.get()
        text_field.config(font=(text_font))

    font_window = Toplevel()
    font_window.title("Font")
    # Set the Geometry of the window.
    font_window.geometry("200x150")
    font_window.minsize(200, 150)
    font_window.maxsize(250, 200)

    selected_font = StringVar(font_window)
    # Set the first options as the initial menu for the dropdown.
    selected_font.set(available_fonts[0])
    # Selector for fonts
    font_selection_drop = OptionMenu(font_window, selected_font, *available_fonts)
    font_selection_drop.pack()

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
    sidebar_frame.pack(fill=Y, side=LEFT)

    titlebar_frame.pack_forget()
    titlebar_frame.pack(side=TOP, fill="x")

    topbar_frame.pack_forget()
    topbar_frame.pack(side=TOP, fill=X)

    text_field_frame.pack_forget()
    text_field_frame.pack(fill=BOTH)


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
    ROOT.title("D-Pad")

    # # Ading an icon
    # ROOT.iconbitmap("win-icon.ico")

    # configuring the base color of the application
    # color => #333842
    ROOT.configure(bg=default_bg)

    # Creating a Frame
    sidebar_frame = Frame(
        ROOT, width=2400, bg=sidebar_color, relief=SUNKEN, borderwidth=4
    )
    # Stretching the sidebar on Y-Axis
    sidebar_frame.pack(side=LEFT, fill=BOTH)

    # Title bar
    titlebar_frame = Frame(ROOT, bg=sidebar_color, relief=FLAT)
    titlebar_frame.pack(side=TOP, fill="x")

    # Topbar
    topbar_frame = Frame(ROOT, bg=topbar_color, relief=FLAT)
    # stretching the topbar on the X-Axis
    topbar_frame.pack(side=TOP, fill="x")

    text_field_frame = Frame(ROOT)
    text_field_frame.pack(fill=BOTH)

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
    file_menu.add_command(
        label="Open a file",
        command=lambda: [open_fileopener(), display_file_address()],
        accelerator="Ctrl + O",
    )
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_command(label="Exit", command=exit, accelerator="Ctrl+W")

    # Edit Menu
    edit_menu = Menu(EDIT_MENU, tearoff=False)
    MAIN_MENU.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl + X")
    edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl + C")
    edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl + V")
    edit_menu.add_separator()
    edit_menu.add_command(label="Font..", command=open_font_selector)

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
        relief=FLAT,
        width=20,
        bg=sidebar_color,
        fg="white",
    )
    sidebar_label.pack(pady=2)

    title_label = Label(
        titlebar_frame,
        text="D-Pad | Text Editor",
        font=("abel", "12", "bold"),
        relief=FLAT,
        background=sidebar_color,
        fg=font_color,
    )
    title_label.pack(pady=6, anchor=CENTER, fill="x")

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

    # Store the input into the
    # text_field
    text_field_content = StringVar(ROOT)
    text_field_content = text_field.get(1.0, END)

    # # Disable the save option
    # # Disable if the text field is empty.
    # if text_field_content == "":
    #     file_menu.entryconfig("Save", state="disabled")

    # if text_field_content != "":
    #     file_menu.entryconfig("Save", state="normal")

    # Running mainloop
    ROOT.mainloop()
