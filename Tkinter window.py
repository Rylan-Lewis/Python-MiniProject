from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

window_root = Tk()
#window specifications
window_root.geometry("700x700")
window_root.minsize(300,300)
window_root.maxsize(800,800)
window_root.configure(background='Yellow')
tx= Label(text="File converter!" , font("Arial" 20),  background="Blue", foreground="Yellow" , width="10", height="5")
tx.configure=(font{"Century gothic", 20})
tx.pack()

#file converter image
photo= PhotoImage(file="minipp.png")
z_label=Label(image=photo)
z_label.pack()



window_root.mainloop()
