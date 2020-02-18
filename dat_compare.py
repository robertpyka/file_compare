
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
    #read path from entry into file path
    file_path = f1_entry.get()
    #open file just to read
    f = open(file_path, "r")
    #create list in loop just with DECL E6POS X 
    dataA= []
    for line in f:
        if line.count('DECL E6POS X') == 1:
            dataA.append(line.strip())
    f.close()
    return dataA
    

def importB():
    #Take data to compare, dataB
    
    file_path = f2_entry.get()
    f = open(file_path, "r")
    #create list in loop just with DECL E6POS X 
    dataB= []
    for line in f:
        if line.count('DECL E6POS X') == 1:
            dataB.append(line.strip())
    f.close()
    return dataB
def green(dataA, dataB,i,j,text1,text2):
    text1.insert(tk.END, dataA[i] + "\n","ok")
    text2.insert(tk.END, dataB[j] + "\n","ok")
    
def red(dataA, dataB,i,j,text1,text2):
    text1.insert(tk.END, dataA[i] + "\n","nok")
    text2.insert(tk.END, dataB[j] + "\n","nok")
    
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
    x = 0
    p = -1
    for i in range(0,lenA):
        #creating just name of point
        added = "false"

        placeA=dataA[i].find("=")
        nameA=dataA[i]
        nameA=nameA[0:placeA]

        for j  in range(0,lenB):
            placeB=dataB[j].find("=")
            nameB=dataB[j]
            nameB=nameB[0:placeB]
            if nameA == nameB and j - p == 1:
                added="true"
                if nameA==nameB and dataA[i] == dataB[j]:
                    green(dataA, dataB,i,j,text1,text2)
                    p = j
                if nameA==nameB and dataA[i] != dataB[j]:
                    red(dataA, dataB,i,j,text1,text2)
                    p = j
            elif nameA == nameB and j - p < 1:
                added = "true"
                text1.insert(tk.END, dataA[i] + "\n","empty")
                text2.insert(tk.END, "\n\n","empty")
            elif nameA == nameB and j - p > 1: 
                l = j
                for k in range(p+1,l):
                    text1.insert(tk.END, "\n\n","empty")
                    text2.insert(tk.END, dataB[k] + "\n","empty")
                if nameA==nameB and dataA[i] == dataB[j]:
                    green(dataA, dataB,i,j,text1,text2)
                    p = j
                if nameA==nameB and dataA[i] != dataB[j]:
                    red(dataA, dataB + "\n",i,j,text1,text2)
                    p = j
                added = "true"
        if added == "false":
            text1.insert(tk.END, dataA[i] + "\n","empty")
            text2.insert(tk.END, "\n\n","empty")
    #adding last elements from dataB without match
    if p<j:
        for a in range(p+1,len(dataB)):
            text1.insert(tk.END, "\n\n","empty")
            text2.insert(tk.END, dataB[a] + "\n","empty")

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

        frame2 = tk.Frame(master=root,bg="blue")
        frame2.pack(fill=tk.BOTH, side=tk.LEFT)
        text2 = tkst.ScrolledText(
            master = frame2,
            wrap   = 'word',  # wrap text at full words only
        )

        text2.pack(fill='both',side=tk.LEFT, expand=True, padx=2)
        compare(dataA, dataB,text1, text2)
        root.mainloop() 
comp_but.bind("<Button-1>", comp_but_click)
wel_wind.mainloop()


