#test okien
#import
import tkinter as tk
import tkinter.scrolledtext as tkst

mytext = '''\
Man who drive like hell, bound to get there.
Man who run in front of car, get tired.
Man who run behind car, get exhausted.
The Internet: where men are men, women are men, and children are FBI agents.
'''
root = tk.Tk()
root.title("ScrolledText")
frame1 = tk.Frame(master=root, width=300)
frame1.pack(fill=tk.Y, side=tk.LEFT)

frame2 = tk.Frame(master=root, width=300)
frame2.pack(fill=tk.Y, side=tk.RIGHT)
text1 = tkst.ScrolledText(
    master = frame1,
    wrap   = 'word',  # wrap text at full words only
    width  = 25,      # characters
    height = 10,      # text lines
    bg='beige'        # background color of edit area
)
# the padx/pady space will form a frame
text1.pack(fill='both', expand=True, padx=8, pady=8)
text1.insert('insert', mytext)


text2 = tkst.ScrolledText(
    master = frame2,
    wrap   = 'word',  # wrap text at full words only
    width  = 25,      # characters
    height = 10,      # text lines
    bg='beige'        # background color of edit area
)
# the padx/pady space will form a frame
text2.pack(fill='both', expand=True, padx=8, pady=8)
text2.insert('insert', mytext)
root.mainloop()
# optiona info
#help(tkst.ScrolledText)
