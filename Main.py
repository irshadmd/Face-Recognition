from tkinter import *
from tkinter import font
import recognizePersonRealTime as fr
import cropFacesAndSave as cf
import findPerson as fp
root = Tk()
root.geometry("480x520")

appHighlightFont = font.Font(family='Helvetica', size=16, weight='bold')
label = Label(root, text="Face Expression and gesture Recognition", fg="red", font=appHighlightFont).place(x=25, y=20)
button1 = Button(root, command=fr.recognizePerson, text="Recognize Face Real Time", activeforeground="blue", height=4,
                 width=25).place(x=150, y=80)
button2 = Button(root, command=cf.cropFacesAndSave, text="Capture faces with date and time in Database",
                 activeforeground="blue", height=4,
                 width=35).place(x=120, y=200)

button3 = Button(root, command=fp.findPerson, text="Find Person from database",
                 activeforeground="blue", height=4,
                 width=35).place(x=120, y=320)

root.mainloop()
