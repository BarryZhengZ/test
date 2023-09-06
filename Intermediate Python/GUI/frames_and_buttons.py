import tkinter as t
import tkinter.messagebox


class myGUI:
   def __init__(self):
       self.main_window = t.Tk()


       self.main_window.geometry('500x200')
       self.main_window.title('Label Demo')


       self.top_frame = t.Frame(self.main_window)
       self.bottom_frame = t.Frame(self.main_window)


       self.label1 = t.Label(self.top_frame,text='John')
       self.label2 = t.Label(self.top_frame,text='Jack')
       self.label3 = t.Label(self.top_frame,text='Jim')


       self.label1.pack(side = "left")
       self.label2.pack(side = "left")
       self.label3.pack(side = "left")


       self.label4 = t.Label(self.bottom_frame,text='Jen')
       self.label5 = t.Label(self.bottom_frame,text='Jill')
       self.label6 = t.Label(self.bottom_frame,text='Jennifer')


       self.label4.pack(side = "left")
       self.label5.pack(side = "left")
       self.label6.pack(side = "left")


       self.top_frame.pack(side = "top")
       self.bottom_frame.pack(side = "top")


       self.mybutton = t.Button(self.main_window,text = "CLick me!", command = self.do_something)
       self.quitbutton = t.Button(self.main_window,text = "Quit!", command = self.main_window.destroy)


       self.mybutton.pack(side = "left")
       self.quitbutton.pack(side = "right")






       t.mainloop()


   def do_something(self):
       tkinter.messagebox.showinfo('Response', "Thanks for clicking the button!")


myinstance = myGUI()


print("moving on......")

