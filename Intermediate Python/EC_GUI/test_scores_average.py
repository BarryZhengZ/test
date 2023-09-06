import tkinter as t
from tkmacosx import Button #downloaded tkmacosx in order to change button color


class TestScoreGUI:
   def __init__(self):
       self.average = 0.0
       self.main_window = t.Tk()
       self.main_window.geometry('400x150')
       self.main_window['background'] = '#3289a8'


       self.top_frame = t.Frame(self.main_window,bg='#3289a8')
       self.mid1_frame = t.Frame(self.main_window,bg='#3289a8')
       self.mid2_frame = t.Frame(self.main_window,bg='#3289a8')
       self.mid3_frame = t.Frame(self.main_window,bg='#3289a8')
       self.bottom_frame = t.Frame(self.main_window,bg='#3289a8')


       self.label1 = t.Label(self.top_frame, text="Enter the score for test 1:",bg='#3289a8',font = "Verdana 14 bold")
       self.score1 = t.Entry(self.top_frame,width=10,bg='#3289a8',bd = 0,font = "Verdana 14 bold",highlightthickness=1,highlightbackground='black')
       self.label1.pack(side = "left")
       self.score1.pack(side = "left")


       self.label2 = t.Label(self.mid1_frame, text="Enter the score for test 2:",bg='#3289a8',font = "Verdana 14 bold")
       self.score2 = t.Entry(self.mid1_frame,width=10,bg='#3289a8',bd = 0,font = "Verdana 14 bold",highlightthickness=1,highlightbackground='black')
       self.label2.pack(side = "left")
       self.score2.pack(side = "left")


       self.label3 = t.Label(self.mid2_frame, text="Enter the score for test 3:",bg='#3289a8',font = "Verdana 14 bold")
       self.score3 = t.Entry(self.mid2_frame,width=10,bg='#3289a8',bd = 0,font = "Verdana 14 bold",highlightthickness=1,highlightbackground='black')
       self.label3.pack(side = "left")
       self.score3.pack(side = "left")


       self.average_label = t.Label(self.mid3_frame, text="Average:",bg='#3289a8',font = "Verdana 14 bold")
       self.average_score_var = t.StringVar()
       self.average_score = t.Label(self.mid3_frame, textvariable=self.average_score_var,bg='#3289a8',font = "Verdana 14 bold")
       self.average_label.pack(side = "left")
       self.average_score.pack(side = "left")




       self.average_button = Button(self.bottom_frame, text="Average", font = "Verdana 14 bold", command=self.calc_average,bg='#3289a8',borderless=1)
       self.quit_button = Button(self.bottom_frame, text="Quit", font = "Verdana 14 bold", command=self.main_window.destroy,bg='#3289a8',borderless=1)
       self.average_button.pack(side = "left")
       self.quit_button.pack(side = "left")


       self.top_frame.pack(side = 'top')
       self.mid1_frame.pack(side = 'top')
       self.mid2_frame.pack(side = 'top')
       self.mid3_frame.pack(side = 'top')
       self.bottom_frame.pack(side = 'top')


       t.mainloop()


   def calc_average(self):
       self.score1 = float(self.score1.get())
       self.score2 = float(self.score2.get())
       self.score3 = float(self.score3.get())


       self.average = round((self.score1 + self.score2 + self.score3)/3,2)
       self.average_score_var.set(self.average)


my_gui = TestScoreGUI()



