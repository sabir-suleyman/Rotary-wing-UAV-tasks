from Tkinter import *
import RPi.GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
pwm = GPIO.PWM(18,100)
pwm.start(5)
GPIO.setwarnings(False)


class App:
	
	def _init_(self,master):
        frame = Frame(master)
	    frame.pack()
	    scale = Scale(frame,from_=0,to  =180, orient=HORIZONTAL,command=self.update)
        scale.grid(row=0)
	
	def uptdate(self,angle):
	    duty = float(angle)/10.0 + 2.5
        pwm.ChangeDutyCycle(duty)

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()