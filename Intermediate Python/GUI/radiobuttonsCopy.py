import tkinter as t
import tkinter.messagebox


class myGUI:
   def __init__(self):
       self.main_window = t.Tk()


       self.main_window.geometry('500x200')
       self.main_window.title('Label Demo')


       self.top_frame = t.Frame(self.main_window)
       self.bottom_frame = t.Frame(self.main_window)


       self.radio_var = t.IntVar()


       self.rb1 = t.Radiobutton(self.top_frame,text = "Option 1", variable = self.radio_var,value = 10, command = self.show_choice)


       self.rb2 = t.Radiobutton(self.top_frame,text = "Option 2", variable = self.radio_var,value = 20)


       self.rb3 = t.Radiobutton(self.top_frame,text = "Option 3", variable = self.radio_var,value = 30)


       self.rb1.pack()
       self.rb2.pack()
       self.rb3.pack()


       self.top_frame.pack(side = "top")
       self.bottom_frame.pack(side = "top")


       self.mybutton = t.Button(self.bottom_frame,text = "OK", command = self.show_choice)
       self.quitbutton = t.Button(self.bottom_frame,text = "Quit!", command = self.main_window.destroy)


       self.mybutton.pack(side = "left")
       self.quitbutton.pack(side = "right")


       t.mainloop()


   def show_choice(self):
       tkinter.messagebox.showinfo('Selection', "The value of the button is " + str(self.radio_var.get()))


myinstance = myGUI()


print("moving on......")

