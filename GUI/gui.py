
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("1600x744")
root.title("Crime Analysis and Prediction")
Tops = Frame(root, width=400, height=50,  relief=SUNKEN)
Tops.pack(side=TOP, fill="y")
Label(Tops, text="Welcome to Crime Analysis and Prediction System\n", font="arial 41 bold", bg="#6666ff", pady=15, anchor='ne').grid(row=0,column=0)
Label(Tops, text="").grid(row=1, column=3)
b1 = Button(root, text="Crime Analysis", font="arial 25 bold", width=15, fg="blue", bg="sky blue", border=6)
Label(Tops, text="").grid(row=1, column=3)
b1.pack(pady=20)

b2 = Button(root, text="Criminal Data", font="arial 25 bold",width=15, fg="blue", bg="sky blue",border=6)
b2.pack(pady=20)

print("\n")
b3 = Button(root, text="Prediction", font="arial 25 bold",width=15,fg="blue", bg="sky blue",border=6)
b3.pack()


# photo = PhotoImage(file="1.png")
# For Jpg Images
# image = Image.open("images.jpg")
# photo = ImageTk.PhotoImage(image)
# varun_label = Label(image=photo)
# varun_label.pack()
# imaginary_tech_root = Tk()
# Width x Height
# imaginary_tech_root.geometry("644x434")
# width, height
# imaginary_tech_root.minsize(300,100)
# width, height
# imaginary_tech_root.maxsize(1200, 988)
# shakaib = Label(text="Shakaib is a good boy and this is his GUI")
# shakaib.pack()
# imaginary_tech_root.mainloop()


root.mainloop()