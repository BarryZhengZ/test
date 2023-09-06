import tkinter as t


class myGUI:
   def __init__(self):
       self.main_window = t.Tk()


       self.main_window.geometry('500x200')
       self.main_window.title('Label Demo')




       self.label1 = t.Label(self.main_window,text='Hello World!')
       self.label2 = t.Label(self.main_window,text='This is my GUI program.')


       self.label1.pack()
       self.label2.pack()


       t.mainloop()


myinstance = myGUI()


print("moving on......")

