from tkinter import *
root = Tk()
def getvals():
    print("It works!")

root.geometry("644x344")
# Heading
Label(root, text="Criminal Record Searching", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)
# Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Crime")
gender = Label(root, text="Gender")
emergency = Label(root, text="Penalitity Period")


# Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)


# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()


# Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)


# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)


Button(text="Search", command=getvals).grid(row=7, column=3)
root.mainloop()
