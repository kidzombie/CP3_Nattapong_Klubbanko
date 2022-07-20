from tkinter import *

def sayHelloWorld():
    print("Hello World!!")

MainWindow = Tk()

text1 = Label(MainWindow,text ="Hello World",width = 20, fg="red",bg="blue",font=("Helvetica",76),anchor=E).grid(row=0,column=1)

MainWindow.mainloop()

