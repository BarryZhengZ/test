import tkinter as t
from tkinter import font
import tkinter.messagebox
from tkmacosx import Button #downloaded tkmacosx in order to change button color


class Registration_Form_GUI:
   def __init__(self):


       self.main_window = t.Tk()
       self.main_window.title("Responsive Registration Form")


       self.frame_title1 = t.Frame(self.main_window)
       self.frame_title2 = t.Frame(self.main_window)
       self.frame_email = t.Frame(self.main_window)
       self.frame_password = t.Frame(self.main_window)
       self.frame_retype_password = t.Frame(self.main_window)
       self.frame_name = t.Frame(self.main_window)
       self.frame_gender = t.Frame(self.main_window)
       self.frame_terms = t.Frame(self.main_window)
       self.frame_newsletter = t.Frame(self.main_window)
       self.frame_register = t.Frame(self.main_window)


       self.label_title1 = t.Label(self.frame_title1, text = "Responsive Registration", font=('Helvetica',20,'bold'))
       self.label_title2 = t.Label(self.frame_title2, text = "Form", font=('Helvetica',20,'bold'))


       def on_entry_click_email(event):
           if self.entry_email.cget('fg') == 'grey':
               self.entry_email.delete(0, "end")
               self.entry_email.insert(0, '')
               self.entry_email.config(fg = 'black')
       def on_focusout_email(event):
           if self.entry_email.get() == '':
               self.entry_email.insert(0, 'Email')
               self.entry_email.config(fg = 'grey')
       self.entry_email = t.Entry(self.frame_email, width=30)
       self.entry_email.insert(0, "Email")
       self.entry_email.bind("<FocusIn>", on_entry_click_email)
       self.entry_email.bind("<FocusOut>", on_focusout_email)
       myfont = font.Font(family="Helvetica",size=13)
       self.entry_email['font']=myfont
       self.entry_email.config(fg="grey")


       def on_entry_click_password(event):
           if self.entry_password.cget('fg') == 'grey':
               self.entry_password.delete(0, "end")
               self.entry_password.insert(0, '')
               self.entry_password.config(fg = 'black',show="*")
       def on_focusout_password(event):
           if self.entry_password.get() == '':
               self.entry_password.insert(0, 'Password')
               self.entry_password.config(fg = 'grey')
       self.entry_password = t.Entry(self.frame_password, width=30)
       self.entry_password.insert(0, "Password")
       self.entry_password.bind("<FocusIn>", on_entry_click_password)
       self.entry_password.bind("<FocusOut>", on_focusout_password)
       self.entry_password['font']=myfont
       self.entry_password.config(fg="grey")


       def on_entry_click_retype(event):
           if self.entry_retype_password.cget('fg') == 'grey':
               self.entry_retype_password.delete(0, "end")
               self.entry_retype_password.insert(0, '')
               self.entry_retype_password.config(fg = 'black',show="*")
       def on_focusout_retype(event):
           if self.entry_retype_password.get() == '':
               self.entry_retype_password.insert(0, 'Re-type Password')
               self.entry_retype_password.config(fg = 'grey')
       self.entry_retype_password = t.Entry(self.frame_retype_password, width=30)
       self.entry_retype_password.insert(0, "Re-type Password")
       self.entry_retype_password.bind("<FocusIn>", on_entry_click_retype)
       self.entry_retype_password.bind("<FocusOut>", on_focusout_retype)
       self.entry_retype_password['font']=myfont
       self.entry_retype_password.config(fg="grey")


       def on_entry_click_fn(event):
           if self.entry_first_name.cget('fg') == 'grey':
               self.entry_first_name.delete(0, "end")
               self.entry_first_name.insert(0, '')
               self.entry_first_name.config(fg = 'black')
       def on_focusout_fn(event):
           if self.entry_first_name.get() == '':
               self.entry_first_name.insert(0, 'First Name')
               self.entry_first_name.config(fg = 'grey')
       self.entry_first_name = t.Entry(self.frame_name,width=14)
       self.entry_first_name.insert(0,"First Name")
       self.entry_first_name.bind("<FocusIn>", on_entry_click_fn)
       self.entry_first_name.bind("<FocusOut>", on_focusout_fn)
       self.entry_first_name['font']=myfont
       self.entry_first_name.config(fg="grey")


       def on_entry_click_ln(event):
           if self.entry_last_name.cget('fg') == 'grey':
               self.entry_last_name.delete(0, "end")
               self.entry_last_name.insert(0, '')
               self.entry_last_name.config(fg = 'black')
       def on_focusout_ln(event):
           if self.entry_last_name.get() == '':
               self.entry_last_name.insert(0, 'Email')
               self.entry_last_name.config(fg = 'grey')
       self.entry_last_name = t.Entry(self.frame_name,width=14)
       self.entry_last_name.insert(0,"Last Name")
       self.entry_last_name.bind("<FocusIn>", on_entry_click_ln)
       self.entry_last_name.bind("<FocusOut>", on_focusout_ln)
       self.entry_last_name['font']=myfont
       self.entry_last_name.config(fg="grey")


       self.label_gender = t.Label(self.frame_gender, text="",anchor="w")
       self.var_gender = t.IntVar()
       self.radio_male = t.Radiobutton(self.frame_gender, text="Male", variable=self.var_gender, value=1,anchor="w")
       self.radio_female = t.Radiobutton(self.frame_gender, text="Female", variable=self.var_gender, value=2,anchor="w")


       self.var_terms = t.IntVar()
       self.check_terms = t.Checkbutton(self.frame_terms, text="I agree with terms and conditions", variable=self.var_terms)


       self.var_newsletter = t.IntVar()
       self.check_newsletter = t.Checkbutton(self.frame_newsletter, text="I want to receive the newsletter", variable=self.var_newsletter)


       Rfont = font.Font(family="Helvetica",size=12,weight="bold")
       self.button_register = Button(self.frame_register, text='Register',command=self.validate,width=300,height=30,background='#42c5f5')
       self.button_register['font']=Rfont


       self.label_title1.pack(side="top")
       self.label_title2.pack(side="top")
       self.entry_email.pack(side="left")
       self.entry_password.pack(side="left")
       self.entry_retype_password.pack(side="left")
       self.entry_first_name.pack(side="left")
       self.entry_last_name.pack(side="left")
       self.radio_male.pack(side="left")
       self.radio_female.pack(side="left")
       self.check_terms.pack(side="left")
       self.check_newsletter.pack(side="left")
       self.button_register.pack(side="left")


       self.frame_title1.pack(pady=1)
       self.frame_title2.pack(pady=1)
       self.frame_email.pack(pady=5,anchor="w")
       self.frame_password.pack(pady=5,anchor="w")
       self.frame_retype_password.pack(pady=5,anchor="w")
       self.frame_name.pack(pady=5,anchor="w")
       self.frame_gender.pack(pady=5,anchor="w")
       self.frame_terms.pack(pady=5,anchor="w")
       self.frame_newsletter.pack(pady=5,anchor="w")
       self.frame_register.pack(pady=5)


       self.main_window.mainloop()


   def validate(self):
       if self.var_gender.get() == 0:
           t.messagebox.showwarning(message = "Please select a gender")
       elif self.var_terms.get() == 0:
           t.messagebox.showwarning(message = "You must agree with terms and conditions")
       elif self.var_newsletter.get() == 0:
           t.messagebox.showwarning(message = "You must check both boxes")
       elif self.entry_password.get() != self.entry_retype_password.get():
           t.messagebox.showwarning(message = "Passwords do not match")
       else:
           t.messagebox.showinfo(message = "Registration Successful")


myinstance = Registration_Form_GUI()





