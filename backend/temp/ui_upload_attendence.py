from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import upload_essl_file_in_out_auto_seperate 

root = Tk()
root.geometry('200x200')

def open_file():
    file = askopenfile(mode='r',filetypes=[('Attendence Files', '*.dat')])
    print(file.name)
    file_loco = file.name
   
    if file is not None:
        print (file_loco)
        upload_essl_file_in_out_auto_seperate.main_method(file.name)

btn = Button(root, text="Upload file", command = lambda:open_file())
btn.pack(side=TOP,pady=10)
mainloop()   