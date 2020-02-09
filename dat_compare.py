
#import GUI
import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as tkst
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

def importA():
    #Take data to compare, dataA

    file_path = f1_entry.get()
    f = open(file_path, "r")
    dataA = f.readlines()
    #variable for new list
    #loop for to create new list, with  useable elements that begins with 'DECL E6POS X'
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
    
    file_path = f2_entry.get()
    f = open(file_path, "r")
    dataB = f.readlines()
    #variable for new list
    #loop for to create new list, with  useable elements that begins with 'DECL E6POS X'
    a = 0
    for i in dataB:
        if i.count('DECL E6POS X') == 1:
            dataB[a] = i
            a=a+1

    #remowing useles elements
    dataB = dataB[0:a]
    return dataB

def compare(dataA, dataB,text1, text2):
#customizng text output
    text1.tag_config("nok", background="yellow", foreground="red")
    text1.tag_config("ok", background="green", foreground="black")
    text1.tag_config("empty", background="blue", foreground="black")
    text2.tag_config("nok", background="yellow", foreground="red")
    text2.tag_config("ok", background="green", foreground="black")
    text2.tag_config("empty", background="blue", foreground="black")
    #check lenght
    lenA = len(dataA)
    lenB = len(dataB)
    
    for i in range(0,lenA):
        #creating just name of point
        added = "false"
        placeA=dataA[i].find("=")
        nameA=dataA[i]
        nameA=nameA[0:placeA]

        for j  in range(0,lenB):
            placeB=dataA[j].find("=")
            nameB=dataB[j]
            nameB=nameB[0:placeB]
            if nameA==nameB and dataA[i] == dataB[j]:
                text1.insert('insert', "\n")
                text1.insert('insert', dataA[i],"ok")
                text2.insert('insert', "\n")
                text2.insert('insert', dataB[j],"ok")
                added = "true"
            if nameA==nameB and dataA[i] != dataB[j]:
                text1.insert('insert', "\n")
                text1.insert('insert', dataA[i],"nok")
                text2.insert('insert', "\n")
                text2.insert('insert', dataB[j],"nok")
                added = "true"
        if added == "false":
            text1.insert('insert', "\n")
            text1.insert('insert', dataA[i],"empty")
            text2.insert('insert', "\n")
            text2.insert('insert', "\n\n","empty")
            
def f1_but_click(event):
#Get filepath from user

    filename = filedialog.askopenfilename(filetypes=[("dat Files", "*.dat"), ("All Files", "*.*")])
    f1_entry.insert(0,filename)
    return "break"
#return "break" keeps button unsunken
f1_but.bind("<Button-1>", f1_but_click)

def f2_but_click(event):
#Get filepath from user
    
    filename = filedialog.askopenfilename(filetypes=[("dat Files", "*.dat"), ("All Files", "*.*")])
    f2_entry.insert(0,filename)
    return "break"
f2_but.bind("<Button-1>", f2_but_click)

def clr_but_click(event):
#Clear all user inputs from entries
    f1_entry.delete(0, tk.END)
    f2_entry.delete(0, tk.END)
clr_but.bind("<Button-1>", clr_but_click)

def comp_but_click(event):
    #import datas to lists
    dataA = importA()
    dataB = importB()
    
    if dataA == dataB:
        #if files are the same,show small window with information
        window = tk.Tk()
        state = tk.Label(window, text="Files match")
        state.pack()
        window.mainloop()

    else:
        #if files are diffrent show large window with listening of those files
        root = tk.Tk()
        root.title("ScrolledText")
        frame1 = tk.Frame(master=root,bg="red")
        frame1.pack(fill=tk.BOTH, side=tk.LEFT)


        text1 = tkst.ScrolledText(
            master = frame1,
            wrap   = 'word',  # wrap text at full words only
            )

        text1.pack(fill='both',side=tk.LEFT, expand=True, padx=2)
        #text1.insert('insert', lenA)

        frame2 = tk.Frame(master=root,bg="blue")
        frame2.pack(fill=tk.BOTH, side=tk.LEFT)
        text2 = tkst.ScrolledText(
            master = frame2,
            wrap   = 'word',  # wrap text at full words only
        )

        text2.pack(fill='both',side=tk.LEFT, expand=True, padx=2)
        #text2.insert('insert', lenB)
        compare(dataA, dataB,text1, text2)
        root.mainloop() 
comp_but.bind("<Button-1>", comp_but_click)
wel_wind.mainloop()


