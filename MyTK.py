from tkinter import *
import tkinter.messagebox

app = Tk()
app.title("Calculator Eval")
app.geometry("500x500")
text_val = StringVar(app)

def calculate():
    getText = str(text_val.get())
    if (getText != ""):
        result = eval(getText)
        tkinter.messagebox.showinfo("infomation", f"Answer is {result}")
        Label(app, text=result, width=10, font=(50)).pack()
    else:
        tkinter.messagebox.showwarning("warning", "Please enter a value")

def deleteText():
    text_val.set("")

def about():
    tkinter.messagebox.showinfo("About", "Developed by: EarthStrix")

def goodbye():
    ask = tkinter.messagebox.askokcancel('Ok Cancel', 'Are You Exit?')
    if (ask == True):
        app.destroy()

menu = Menu(app)
menu.add_command(label="About" ,command=about)
menu.add_command(label="Exit" ,command=goodbye)

app.config(menu=menu)

label = Label(app, text="Calculator Eval",
              width=15, height=2, font=(50)).pack()
text_ = Entry(app, textvariable=text_val, width=30 ,font=(90)).pack(ipadx=10, ipady=8)
btn = Button(app, text="Equal", width=10, height=2, font=(50),command=calculate).pack()
btn2 = Button(app, text="Clear", width=10, height=2, font=(50), command=deleteText).pack()
Label(app, text="----------------HISTORY--------------",
      width=15, font=(50)).pack(padx=20, pady=20)

app.mainloop()
