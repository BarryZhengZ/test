import tkinter as t
import tkinter.messagebox


class myGUI:
   def __init__(self):
       self.main_window = t.Tk()


       self.main_window.geometry('500x200')
       self.main_window.title('Label Demo')


       self.top_frame = t.Frame(self.main_window)
       self.bottom_frame = t.Frame(self.main_window)


       self.cb_var1 = t.IntVar()
       self.cb_var2 = t.IntVar()
       self.cb_var3 = t.IntVar()


       self.cb1 = t.Checkbutton(self.top_frame,text = "Option 1", variable = self.cb_var1)


       self.cb2 = t.Checkbutton(self.top_frame,text = "Option 2", variable = self.cb_var2)


       self.cb3 = t.Checkbutton(self.top_frame,text = "Option 3", variable = self.cb_var3)


       self.cb1.pack()
       self.cb2.pack()
       self.cb3.pack()


       self.top_frame.pack(side = "top")
       self.bottom_frame.pack(side = "top")


       self.mybutton = t.Button(self.bottom_frame,text = "OK", command = self.show_choice)
       self.quitbutton = t.Button(self.bottom_frame,text = "Quit", command = self.main_window.destroy)


       self.mybutton.pack(side = "left")
       self.quitbutton.pack(side = "right")

       t.mainloop()


   def show_choice(self):
       self.message = 'You selected :\n'


       if self.cb_var1.get() == 1:
           self.message += '1\n'
       if self.cb_var2.get() == 1:
           self.message += '2\n'
       if self.cb_var3.get() == 1:
           self.message += '3\n'    


       tkinter.messagebox.showinfo('Selection',self.message)


myinstance = myGUI()


print("moving on......")

