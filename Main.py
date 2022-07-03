from base64 import b64encode
from tkinter import *
from tkinter import font   
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from PyPDF2 import PdfFileMerger, PdfFileReader
import re
from pathlib import Path
import os
import subprocess
import tabula
from pdf2docx import Converter
from docx2pdf import convert
from PyPDF2 import PdfFileWriter, PdfFileReader

proot= Tk()
proot.title("Validation Window")
proot.geometry("800x800")
proot.maxsize(800,800)
proot.minsize(500,500)
px=Label(proot, text="ENTRY GATE", font=("Calibri",15, "italic"), bg="White", fg="Black", width=12, height=1, relief=SUNKEN, padx= 20, pady=10)
px.pack()
key1=Label(proot, text='To convert your files, Enter the Passkey:', font=("Calibri", 15))
key1.pack()
pa1= StringVar() 
pa1e= Entry(proot,textvariable=pa1)
pa1e.pack()

photo= PhotoImage(file="minipp.png")
z_label=Label(image=photo)
z_label.pack()

def check():
    a=pa1.get()
    pattern = r"\A(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@%&])[A-Za-z\d@%&]{5,10}$"
    x = re.search(pattern,a)
    
    if x:
        window_root = Tk()
        #window specifications
        window_root.geometry("1000x1000")
        window_root.minsize(300,300)
        window_root.maxsize(800,800)
        window_root.configure(background='Grey')
        window_root.title("FILE CONVERTER SYSTEM")
        tx= Label(window_root,text="Convert your Files!" , font={"Arial", 20, "bold"},  background="Red", foreground="White" , width="12", height="1", relief=SUNKEN, padx=20, pady=10)
        tx.pack()
        window_root.mainloop()
        
        #Pdf to word conversion
        def p():
            docx_file='Converted Word file.docx'
            filp = askopenfile(filetypes=[('Pdf Files', '*.pdf')])
            pv = Converter(filp.name, r'C:\Users\lenovo\Desktop\Mini project python')
            pv.convert(docx_file)
            showinfo("Converted to Word")
            pv.close()
        frame1 = Frame(window_root)
        frame1.pack( padx=20, pady = 20)
        b1=Button(frame1, fg='red', text="Convert Pdf file to Word file", relief="sunken", command=p)
        b1.pack(side=TOP, padx=10, pady=10)
    else:
        showinfo("INVALID")
        

pb=Button(proot, text='Validate', command=check)
pb.pack()

proot.mainloop()
