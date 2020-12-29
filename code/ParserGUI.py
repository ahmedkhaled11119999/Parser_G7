import os
dirpath = os.getcwd()
os.environ["PATH"] += os.pathsep + dirpath + os.pathsep + 'graphviz-2.38\\release\\bin'
from tkinter import *
from tkinter import Entry
from tkinter.filedialog import askopenfilename
import tkinter as tk
import grammar as gr


from stp import return_tokens
win = tk.Tk()
var = IntVar()
def readfromfile(INPUTFILE):
    inFile = open(INPUTFILE, 'r') # read from file
    lines = inFile.readlines()
    inFile.close()
    return lines
def main(lines):
    gr.outputs = return_tokens(lines)
    gr.program()
    gr.generate_tree()



win.iconbitmap("parser_icon.ico")
win.title("Parser 2020")
win.configure(background='#8F0000')
win.geometry("700x600")
win.resizable(False,False)

#----------------------------
#labels in the middle
#----------------------------

label1 = tk.Label(win, text="No option is selected!!",bg='#8F0000', fg="white")
label1.pack()
label2 = tk.Label(win, text="Status: (waiting for inputs)", bg='#8F0000',  fg="white")
label2.pack()
label3 = tk.Label(win, text="", bg='#8F0000', fg="white")
label3.pack()

#----------------------------
#TINY label in the LEFT
#----------------------------

Tiny = tk.Label(win , text= "Parser G7", width= 17, height= 2, bg = "white", fg= "#683838 ")
Tiny.pack()
Tiny.place(bordermode=INSIDE, x=0,y = 10)
#----------------------------
#Our names in the right
#----------------------------
Tiny = tk.Label(win , text= "Ahmed Khaled\nOmar Hany\nAhmed Gamal\nEslam Asfour", width= 17, height= 5, bg = "white", fg= "#683838")
Tiny.pack()
Tiny.place(bordermode=INSIDE, x=575,y = 10)
#----------------------------
#label above RUN button
#----------------------------

L1 = tk.Label(win , text= "Click Run to parse Tiny Code:", bg="#8F0000", fg="white")
L1.pack()
L1.place(bordermode=INSIDE, x=520, y=505)

L5 = tk.Label(win , text= "Click Show to review Tiny Code:", bg="#8F0000", fg="white")
L5.pack()
L5.place(bordermode=INSIDE, x=20, y=505)
#----------------------------
#label above RADIO BUTTON
#----------------------------

L2 = tk.Label(win , text= "Choose your preferred method: (File Path/Tiny Code)", bg="#8F0000", fg="white")
L2.pack()
L2.place(bordermode=INSIDE, x=10, y=65)

#----------------------------
#Entry of Directory
#----------------------------

E1 = Entry(win, width = 70,bg="white", fg="#8F0000")
E1.pack()
E1.place(bordermode=OUTSIDE, x=100, y=145)

#----------------------------
#Entry of Tiny Code
#----------------------------

E2 = Text(win, width = 84, height = 17 ,bg="white", fg="#8F0000")
E2.pack()
E2.place(x= 10, y= 210)

#----------------------------
#label above File Path Entry
#----------------------------

Dir = tk.Label(win , text= "Enter File Path:", bg="#8F0000", fg="white")
Dir.pack()
Dir.place(bordermode=INSIDE, x=10, y=145)

#----------------------------
#label above Tiny Code Entry
#----------------------------

Code = tk.Label(win , text= "Enter Tiny Code:", bg="#8F0000", fg="white")
Code.pack()
Code.place(bordermode=INSIDE, x=10, y=180)

#----------------------------
#Functions:
#----------------------------

def sel():
   selection = "You selected the option " + str(var.get())
   label1.config(text = selection)
   x = var.get()
   if x == 1:
       label3.config(text="File Path")
       E2.config(state='disabled')
       E1.config(state='normal')
       E2.delete(0, END)
   elif x ==2:
       label3.config(text="Tiny Code")
       E1.config(state='disabled')
       E2.config(state='normal')
       E2.delete('1.0', END)
       E1.delete(0, END)

def main_RUN():
    x = var.get()
    if(x==1):
        if(len(Entry.get(E1))):
            label2.config(text="Status: Tiny Code is Running...")
            lines = readfromfile(Entry.get(E1))
            main(lines)
        else:
            label2.config(text="Status: Error, please enter File Path at first!")
    elif(x==2):
        if(len(E2.get(1.0, END)) > 1):
            label2.config(text="Status: Tiny Code is Running...")
            lines = E2.get(1.0, END)
            lines = lines.split()
            main(lines)
        else:
            label2.config(text="Status: Error, please enter Tiny Code at first!")
    else:
        label2.config(text="Status: Error, please select an entry method!")
def OpenFileGui():
    filename = askopenfilename()
    if(len(Entry.get(E1))):
        E1.delete(0,END)
    E1.insert(END,filename)
def show():
    if(len(Entry.get(E1))):
        lines = readfromfile(Entry.get(E1))
        E2.config(state='normal')
        E2.delete('1.0', END)
        lines = "".join(lines)
        E2.insert(END,lines)
    else:
        label2.config(text="Status: Error, please select a File Path first!")
#----------------------------
#Buttons:
#----------------------------

R1 = Radiobutton(win, text = "File Path", selectcolor= "#8F0000", highlightcolor = "white", activebackground="#8F0000", bg="#8F0000", fg="white", variable = var, value = 1, command = sel)
R1.pack()
R1.place(bordermode=OUTSIDE, x=20, y=100)

R2 = Radiobutton(win, text = "Tiny Code", selectcolor= "#8F0000", highlightcolor = "white", activebackground="#8F0000", bg="#8F0000", fg="white", variable = var, value = 2, command = sel)
R2.pack()
R2.place(bordermode=OUTSIDE, x=130, y=100)
Run = tk.Button(win, text = "Run", command = main_RUN,  width = 10,activebackground= "white", activeforeground = "#8F0000")
Run.pack()
Run.place(x=595, y=540)
OpenFile = tk.Button(win, text = "Open File", command = OpenFileGui,  width = 10,activebackground= "white", activeforeground = "#8F0000")
OpenFile.pack()
OpenFile.place(x=595, y=144)
SHOW = tk.Button(win, text = "Show", command = show, width = 10,activebackground= "white", activeforeground = "#8F0000")
SHOW.pack()
SHOW.place(x=20, y=540)

win.mainloop()

