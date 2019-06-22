'''
Main Menu for 2.5 Axis CNC Machine Based on Raspberry Pi 3,
AdaFruit Motor Hat (AdaFruit Motor Hat Library), and Arduino Uno
'''

import Tkinter
from tweet2Inx import *
from inx2Gcode import *
from gcode2Steps import *
from steps2Motion import *

while True:

    #Main Menu
    root1 = Tkinter.Tk()
    text1 = "Push the Button Below to Print a Tweet"

    def confirmMessage():
        root1.destroy()

    label1 = Tkinter.Label(root1, text=text1,font=("Courier", 44), wraplength = 500)
    button1 = Tkinter.Button(font=("Courier", 44), text="Print", command = confirmMessage)

    label1.pack()
    button1.pack()
    root1.mainloop()

    
    #Confirmation Message
    root2 = Tkinter.Tk()
    text2 = "Your Tweet is Now Printing"

    label2 = Tkinter.Label(root2, text=text2,font=("Courier", 44), wraplength = 500)
    root2.after(3000,lambda: root2.destroy())

    label2.pack()
    root2.mainloop()

    #Printing Functions
    tweet2Inx()
    inx2GCode()
    stepCounter = gcode2Steps()
    steps2Motion(stepCounter)

    #End Message
    root3 = Tkinter.Tk()
    text3 = "Your Tweet Has Printed"

    label3 = Tkinter.Label(root3, text=text3,font=("Courier", 44), wraplength = 500)
    root3.after(3000,lambda: root3.destroy())

    label3.pack()
    root3.mainloop()
    