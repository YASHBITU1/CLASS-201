from tkinter import *


def Calc():
    p = float(username.get())
    r = float(weight.get())
    t = float(height.get())
    i = (p*r*t)/100
    
    interest = round(i,2)   
    
    outputmessage = Label(frame,text=",Interest:"+str(interest),bg="white",font=("Calibri",15),bd=5,width=40)
    outputmessage.place(x=20,y=370)
    outputmessage.pack()
    
    
    

window = Tk()
window.title("SIMPLE INTEREST")
window.geometry("400x600")
window.configure(bg="lightblue")

heading = Label(window,text="INTEREST CALC",fg="blue",bg="black",font=("Calibri",20),bd=5)
heading.place(x=20,y=20)

yourname = Label(window,text="principle",fg="white",bg="black",font=("Calibri",20),bd=5)
yourname.place(x=20,y=70)

username = Entry(window,text="",bd=3,width=50)
username.place(x=20,y=120)

yourweight = Label(window,text="Rate of Interest",fg="white",bg="black",font=("Calibri",20),bd=5)
yourweight.place(x=20,y=160)

weight = Entry(window,text="",bd=3,width=50)
weight.place(x=20,y=200)

yourheight = Label(window,text="Time",fg="white",bg="black",font=("Calibri",20),bd=5)
yourheight.place(x=20,y=240)

height = Entry(window,text="",bd=3,width=50)
height.place(x=20,y=290)

button = Button(window,text="CALCULATE",fg="white",bg="black",font=("Calibri",20),bd=5,command=Calc)
button.place(x=20,y=330)

frame = LabelFrame(window,text="RESULT",bg="white",font=("Calibri",20),bd=5)
frame.pack(padx=60,pady=60)
frame.place(x=20,y=420)

text = Label(frame,text="------",bg="white",font=("Calibri",20),bd=5,width=30)
text.place(x=10,y=20)
text.pack()


    
    



window.mainloop()