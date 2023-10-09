
# A password generator is a useful tool that generates strong andrandom passwords for users. 
# This project aims to create apassword generator application using Python, 
# allowing users tospecify the length and complexity of the password. 
# User Input: Prompt the user to specify the desired length of thepassword.
# Generate Password: Use a combination of random characters togenerate a password of the specified length.
# Display the Password: Print the generated password on the screen.

from tkinter import *
from random import randint

root = Tk()
root.title('Password Generator')
root.geometry("500x300")

def new_rand():
    # Clear Entry Box
    pw_entry.delete(0, END)
    
    # Get PW length
    pw_length = int(my_entry.get())

    # Create Password
    my_password = ''
    
    for x in range(pw_length):
        my_password += chr(randint(33,126))
        
    pw_entry.insert(0, my_password)

def clipper():
    # Clear Clipboard
    root.clipboard_clear()
    
    # Copy to Clipboard
    root.clipboard_append(pw_entry.get())

# Label Frame
lf = LabelFrame(root, text="How Many Chanracters: ")
lf.pack(pady=20)

# Entry Box
my_entry = Entry(lf, font=("Helvatica", 24))
my_entry.pack(pady=20, padx=20)

# Entry Box for Copying Label
pw_entry = Entry(root, text='', font=("Helvatica", 24),bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

# Frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# Buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0,column=0, padx=10)

clip_button = Button(my_frame, text="Copy to Clipboard.", command=clipper)
clip_button.grid(row=0, column=1, padx=10)


root.mainloop()
