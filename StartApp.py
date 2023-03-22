# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 04:23:11 2022
@author: Azmi Deliaslan
"""
#First Screen
from tkinter import *
from tkinter.ttk import Progressbar
import sys
import os
import time

root = Tk()

#creating image var
image = PhotoImage(file='images\\first_screen.png')
#size of the window in pixels
height = 450
width = 600
#The x and y variables are used to calculate the position of the window on the screen, so that it is centered horizontally and vertically.
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
#get the dimensions of the screen, in pixels. The window is then positioned in the center of the screen by dividing these dimensions by 2 and subtracting half the width and height of the window.
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#remove the window frame and title bar from the root window. This makes the window appear as a floating window without any borders or decorations.
root.overrideredirect(1)
#The '-topmost' attribute is a Tkinter attribute that can be used to control the stacking order of windows.
root.wm_attributes('-topmost', True)
root.config(background='#ffffff')
#background image
bg_label = Label(root, image=image)
bg_label.place(x=0, y=0)

welcome_label = Label(text='Welcome to Inventory Management System', bg='black', font=("arial", 15, "bold"), fg='white')
welcome_label.place(x=100, y=20)

created_by_label = Label(text='Created By SatDeliaslan', bg='black', font=("arial", 15, "bold"), fg='white')
created_by_label.place(x=170, y=50)

progress_label = Label(root, text="Please Wait...", font=('arial', 13, 'bold'), fg='white',bg='black')
progress_label.place(x=225, y=350)
progress = Progressbar(root, orient=HORIZONTAL, length=550, mode='determinate')
progress.place(x=25, y=390)

exit_btn = Button(text='x', bg='red', command=lambda: exit_window(), bd=0, font=("arial", 16, "bold"),
                  activebackground='#fd6a36', fg='white')
exit_btn.place(x=570, y=0)
def exit_window():
    sys.exit(root.destroy())

def top():
    root.withdraw()
    os.system("python productManager.py")
    root.destroy()
i = 0

def loadsystem():
    global i
    if i <= 100:
        if i == 90:
            time.sleep(2)
        txt = 'Please Wait...  ' + (str(i)+'%')
        progress_label.config(text=txt)
        progress_label.after(10, loadsystem)
        progress['value'] = i
        i += 1
    else:
        top()

loadsystem()
root.mainloop()

