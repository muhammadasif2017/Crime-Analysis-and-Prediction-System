
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("600x344")
root.title("Crime Analysis and Prediction")
Tops = Frame(root, width=400, height=40,  relief=SUNKEN)
Tops.pack(side=TOP, fill="y")
Label(Tops, text="Criminal Record\n", font="arial 25 bold", bg="sky blue", pady=5, width=25).grid(row=0,column=0)
Label(Tops, text="").grid(row=1, column=3)
b1 = Button(root, text="Enter New Criminal Record ", font="arial 15 bold", width=25, fg="blue", bg="sky blue", border=6)
Label(Tops, text="").grid(row=1, column=3)
b1.pack(pady=20)
b2 = Button(root, text="Search Data", font="arial 15 bold",width=25, fg="blue", bg="sky blue",border=6)
b2.pack(pady=20)
root.mainloop()