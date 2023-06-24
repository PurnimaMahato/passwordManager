from tkinter import *
from tkinter import ttk
import hashlib
import pyperclip
import pickle
import tkinter.messagebox


file="MyData.pkl"
fileobj = open(file , 'rb')
password = pickle.load(fileobj)
length1 = len(password)

win = Tk()
win['bg']='#7FFFD4'

win.title("Password Manager")
style = ttk.Style()
style.theme_use('default')
style.configure('Treeview.Heading', background="orange",font = ('arial', 15,'bold'))
style.configure('Treeview',font = ('Calibri', 12,'bold') )

encrypted = []
decrypted = []
Sites = ["Google" , "Facebook" , "Instagram"]
treelist = []

     
tree = ttk.Treeview(win, column=("Site", "Password"), show='headings', height=5,selectmode="browse")
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Site")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Password")


for i in range(0 ,length1):
    
    encpass = hashlib.sha1(password[i].encode())
    encrypted.append(encpass)
    

def ButtonOnclick():
    for k in range(len(treelist)):
       if treelist[k] == tree.focus():
        pyperclip.copy(password[k])
        tkinter.messagebox.showinfo("","Woohoo!!Password copied :) ")


for j in range(length1):
    
    passEnc =encrypted[j].hexdigest()
    treelist.append (tree.insert('',j, values=(Sites[j], passEnc)))
    
treeScroll = ttk.Scrollbar(win)
treeScroll.configure(command=tree.yview)
tree.configure(yscrollcommand=treeScroll.set)
treeScroll.pack(side= RIGHT, fill= BOTH)
tree.pack() 
Button(win, text ="copy",command=ButtonOnclick,background = "blue",foreground = "white",activebackground="green", activeforeground="#fff").pack(padx=10 , pady=10,ipadx=8,ipady=3)    
win.mainloop()
