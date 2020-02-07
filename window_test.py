#test okien
#import
import tkinter as tk
from tkinter import filedialog
from tkinter import *
wel_wind = tk.Tk()

#configuration of welcome window
wel_wind.rowconfigure([0,1], minsize=10, weight=1)
wel_wind.columnconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)

#adding components, 2 entries, 2 labes and 4 buttons
f1_lab = tk.Label(wel_wind, text="Choose file 1")
f1_lab.grid(row = 0, column = 0)
f1_entry = tk.Entry()
f1_entry.grid(row = 1, column = 0, padx = 5)
f1_but = tk.Button(text ="...",width = 5, height = 1)
f1_but.grid(row = 1, column = 1,padx=5)
f2_lab = tk.Label(wel_wind, text="Choose file 2")
f2_lab.grid(row = 2, column = 0)
f2_entry = tk.Entry()
f2_entry.grid(row = 3, column = 0, padx = 5)
f2_but = tk.Button(text ="...",width = 5, height = 1)
f2_but.grid(row = 3, column = 1,padx=5, pady = 5)
comp_but = tk.Button(text = "Compare",width = 10, height = 1)
comp_but.grid(row = 4, column = 1,padx=5, pady = 5, sticky = "w")
clr_but = tk.Button(text = "Clear",width = 10, height = 1)
clr_but.grid(row = 4, column = 0,padx=5, pady = 5, sticky = "e")

def f1_but_click(event):
#Get filepath from user

    filename = filedialog.askopenfilename()
    f1_entry.insert(0,filename)
    return "break"
#return "break" keeps button unsunken
f1_but.bind("<Button-1>", f1_but_click)

def f2_but_click(event):
#Get filepath from user
    
    filename = filedialog.askopenfilename()
    f2_entry.insert(0,filename)
    return "break"
f2_but.bind("<Button-1>", f2_but_click)

def clr_but_click(event):
#Clear all user inputs from entries
    f1_entry.delete(0, tk.END)
    f2_entry.delete(0, tk.END)
clr_but.bind("<Button-1>", clr_but_click)
wel_wind.mainloop()
