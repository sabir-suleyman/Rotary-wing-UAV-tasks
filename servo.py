from tkinter import *
import RPi.GPIO as io
import time
io.setmode(io.BOARD)
io.setup(11,io.OUT)
p=io.PWM(11,50)
p.start(2.5)
root = Tk()
Label(root, text="Angle").grid(row=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

def cal():
    global dc
    deg1 =e1.get()
    deg = abs(float(deg1))
    dc = 0.056*deg + 2.5
    p.ChangeDutyCycle(dc)
    print(deg, dc)
   
b1= Button(root, text = "Enter",bg="pink", command =cal)
b1.grid(row=2, column=1)
b3 = Button(root, text='Quit', bg= "cyan", command=root.quit)
b3.grid(row=2, column=3)
root.mainloop()