
# Task 1: TO-DO LIST

# A To-Do List application is a useful project that helps users manage
# and organize their tasks efficiently. This project aims to create a
# command-line or GUI-based application using Python, allowing
# users to create, update, and track their to-do lists.

from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle


# Main Window
app = Tk()
app.title("To - Do List App!!")
app.geometry("600x600")

my_font = Font(
    family="Inter",
    size=30,
    weight="bold"
)

# Frames and Buttons
my_frame = Frame(app)
my_frame.pack(pady=10)

button_frame = Frame(app)
button_frame.pack(pady=20)

# Listbox
my_list = Listbox(my_frame,
    font=my_font,
    width=25,
    height=5,
    bg= "SystemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"
)

my_list.pack(side=LEFT, fill=BOTH)

# stuff = ["Walk the dog", "Buy groceries", "Learn Tkinter", "Rise and Conquer the World"]

# for item in stuff:
#     my_list.insert(END, item)

# Scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Configuring List and Scroll Bar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Entry Box
my_entry = Entry(app, font=("Helventica", 24), width=26)
my_entry.pack(pady=20)

# Functions to handle list actions
def delete_item():
    my_list.delete(ANCHOR)


def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)


def cross_off_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede"
    )
    my_list.selection_clear(0, END)


def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646"
    )
    my_list.selection_clear(0, END)

def del_crossed_item():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1

def save_list():
    file_name = filedialog.asksaveasfile(
        initialdir="D:/StudyMaterial/Internship/Codsoft/Task 1",
        title="Save File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*")
        )  
    )

    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

        count = 0    
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count += 1

        stuff = my_list.get(0, END)

        output_file = open(file_name, 'wb')
        pickle.dump(stuff, output_file)


def open_list():
    file_name = filedialog.askopenfile(
        initialdir="D:/StudyMaterial/Internship/Codsoft/Task 1",
        title="Open File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*")
        ) 
    )

    if file_name:
        my_list.delete(0, END)

        input_file = open(file_name, 'rb')

        stuff = pickle.load(input_file)

        for item in stuff:
            my_list.insert(END, item)
    
def clear_list():
    my_list.delete(0, END)
    pass

# Create Buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)
del_crossed_button = Button(button_frame, text="Delete Crossed Items", command=del_crossed_item)


delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1, padx=20)
cross_off_button.grid(row=0,column=2)
uncross_button.grid(row=0,column=3, padx=20)
del_crossed_button.grid(row=0, column=4)

# Create Menu
my_menu = Menu(app)
app.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)


file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)

app.mainloop()

