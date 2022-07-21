from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    BMI = round(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2),2)
    BMIDefine = ""
    if BMI < 18.5:
        BMIDefine = "ผอมเกินไป"
    elif BMI < 23.0:
        BMIDefine = "ปกติ"
    elif BMI < 25.0:
        BMIDefine = "น้ำหนักเกิน"
    elif BMI < 30.0:
        BMIDefine = "อ้วน"
    else:
        BMIDefine = "อ้วนมาก"

    text1 = "BMI : "+ str(BMI) +" คุณ"+ BMIDefine
    labelResult.configure(text= text1)



MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="ตำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()

print("1")
