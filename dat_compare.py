
#import
import tkinter as tk
from tkinter import filedialog
    
def importA():
    #Take data to compare, dataA

    #File dialog
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    f = open(file_path, "r")
    dataA = f.readlines()
    #variable for new list
    #loop for to create new list, with  useable elements at the begin 'DECL E6POS X'
    a = 0
    for i in dataA:
        if i.count('DECL E6POS X') == 1:
            dataA[a] = i
            a=a+1

    #remowing useless elements
    dataA = dataA[0:a]
    return dataA
    

def importB():
    #Take data to compare, dataB


    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    f = open(file_path, "r")
    dataB = f.readlines()
    #variable for new list
    #loop for to create new list, with  useable elements at the begin 'DECL E6POS X'
    a = 0
    for i in dataB:
        if i.count('DECL E6POS X') == 1:
            dataB[a] = i
            a=a+1

    #remowing useles elements
    dataB = dataB[0:a]
    return dataB

# main
dataA = importA()
dataB = importB()
if dataA == dataB:
    window = tk.Tk()
    greeting = tk.Label(window, text="Files match")
    greeting.pack()
    window.mainloop()

else:
    window = tk.Tk()
    greeting = tk.Label(window, text=dataB)
    greeting.pack()
    window.mainloop()
