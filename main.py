# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:22:40 2020

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:09:40 2020

@author: Admin
"""

from tkinter import *
from tkinter.filedialog import *
from autocomplete import models
import autocomplete


filename = None

def loadHarry():
    models.load_models("pklFiles\harryPorter.pkl")


def loadAlice():
    models.load_models("pklFiles\wonderland.pkl")

def loadGOT():
    models.load_models("pklFiles\gameOfthrones.pkl")


def newFile():
    global filename
    filename =  "Utitled"
    text.delete(0.0,END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename,'w')
    f.write()
    f.close()

def saveAs():
    f = asksaveasfile(mode='w',defaultextension='.txt')
    t = text.get(0.0 ,END)
    try:
        f.write(t.strip())
    except:
        showerror(title="Oops!",message="unable to save file...")
        
def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0 , END)
    text.insert(0.0,t)
    
root = Tk()
root.title("Editor")
root.minsize(width=400,height=400)
root.maxsize(width=400 ,height=400)

text = Text(root,width=400,height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=newFile)
filemenu.add_command(label="Safe as ...",command=saveAs)
    
filemenu.add_command(label="Harry Porter",command=loadHarry)
filemenu.add_command(label="Alice in Wonderland",command=loadAlice)
filemenu.add_command(label="Game Of Thrones",command=loadGOT)


filemenu.add_command(label='Quit',command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

olddata1 = None
olddata2 = None   
data1 = None 
data2 = None
def predict():
    global data1,data2,olddata1,olddata2
    if(len(text.get(0.0,END).split()) > 1):
        data1 , data2 = text.get(0.0,END).split()[-2:]
    if(not (data1 == olddata1 and data2 == olddata2)):
        olddata1 = data1
        olddata2 = data2
        try:    
            print(autocomplete.predict(data1,data2))
        except:
            print("[]")
    root.after(20, predict)

root.config(menu=menubar)
root.after(20, predict)
root.mainloop()



