#test okien
#import
import tkinter as tk

wel_wind = tk.Tk()

for i in range(5):
    for j in range(2):
        frame = tk.Frame(  
            master=wel_wind,
            relief=tk.RAISED,
            borderwidth=1
            )
        frame.grid(row=i, column=j, padx=5, pady=5)

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
wel_wind.mainloop()
