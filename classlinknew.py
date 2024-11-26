from tkinter import *
import webbrowser
from PIL import Image, ImageTk

def openDS():
    webbrowser.open('https://drive.google.com/drive/folders/1QRBBfykNCSIyM5Sf-A2qLTHJwe15jCvz?usp=sharing')
def openMath():
    webbrowser.open('https://drive.google.com/drive/folders/1gPEet1vzrOMTL_YJXDGgGKuolzpqmoEJ?usp=sharing')
def openDE():
    webbrowser.open('https://drive.google.com/drive/folders/1TS3t8fu4OHz6E8x7ykeJpvHv5QL59Vay?usp=sharing')
def openPOM():
    webbrowser.open('https://drive.google.com/drive/folders/1A_T1QIxJv8ptNR4gFaeH3T8x8nEkkpTA?usp=sharing')
def openDBMS():
    webbrowser.open('https://drive.google.com/drive/folders/13qEEt1m0wrXm4rcZ-6TGU0-jhunSokpT?usp=sharing')

window=Tk()
window.geometry("400x500")
#window.configure(bg='#483D8B')
window.title("CLASS LINK 2.0")

maths=PhotoImage(file="\\classimg\\math.png")
vs=PhotoImage(file="\\classimg\\vs.png")
oops=PhotoImage(file="\\classimg\\oops.png")
poa=PhotoImage(file="\\classimg\\poa.png")
cpp=PhotoImage(file="\\classimg\\cpp.png")
Label(window,text="_"*27,font=("Arial",20,"bold")).place(x=0,y=30)
Label(window,text="Click and Browse recordings",font=("Arial",20,"bold"),fg="#9932CC").place(x=10,y=20)
but1=Button(window,command=openDS,image=maths,bd=0)
but2=Button(window,command=openMath,image=vs,bd=0)
but3=Button(window,command=openDE,image=oops,bd=0)
but4=Button(window,command=openPOM,image=poa,bd=0)
but5=Button(window,command=openDBMS,image=cpp,bd=0)

but1.place(x=50,y=90)
but2.place(x=250,y=90)
but3.place(x=50,y=215)
but4.place(x=250,y=215)
but5.place(x=50,y=340)

window.mainloop()
