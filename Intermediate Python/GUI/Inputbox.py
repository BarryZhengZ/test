import tkinter as t
import tkinter.messagebox


class KilConverterGUI:
   def __init__(self):
       self.main_window = t.Tk()


       self.main_window.geometry('500x200')
       self.main_window.title('Label Demo')


       self.top_frame = t.Frame(self.main_window)
       self.bottom_frame = t.Frame(self.main_window)


       self.prompt_label = t.Label(self.top_frame,text = "Enter a distance in Kilometers: ")
       self.kilo_entry = t.Entry(self.top_frame, width = 10)


       self.prompt_label.pack(side = "left")
       self.kilo_entry.pack(side = "left")


       self.top_frame.pack(side = 'top')
       self.bottom_frame.pack(side = 'top')


       self.calc_button = t.Button(self.bottom_frame,text = "Convert",command = self.convert)
       self.quitbutton = t.Button(self.bottom_frame,text = "Quit",command = self.main_window.destroy)


       self.calc_button.pack(side = "left")
       self.quitbutton.pack(side = "left")

       t.mainloop()


   def convert(self):
       kilo = float(self.kilo_entry.get())
       miles = round(kilo * 0.6214,2)
       tkinter.messagebox.showinfo('Result', str(kilo) + 'kilometers is equal to ' + str(miles) + ' miles')


myinstance = KilConverterGUI()


print("moving on......")

