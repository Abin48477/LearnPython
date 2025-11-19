from tkinter import *;

root = Tk()
#creating a label, widget
myLabel1 = Label(root, text="Hello World!")
myLabel1.grid(row=0, column=0)# it helps to put the label onto the screen


def myclick():
    myLabel2= Label(root, text="Look! I Clicked! a button")
    myLabel2.grid(row=0,column=2)
    
mybutton = Button(root, text="Click Me!" ,padx=50, pady=20,fg="blue", bg="yellow", command=myclick)
mybutton.grid(row=1, column=1)

   
root.mainloop() #it helps to run the window continuously
