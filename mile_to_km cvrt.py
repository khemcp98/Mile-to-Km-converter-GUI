from tkinter import *

window = Tk()
window.title("Mile to KM")
window.minsize(width=250,height=100)
window.config(padx=20,pady=20)

entry_mile = Entry(width=10)
entry_mile.grid(row=0,column=1)
# entry_mile.config(padx=20,pady=20)

label_mile = Label(text="Mile")
label_mile.grid(row=0,column=2)
label_mile.config(padx=5,pady=5)

label =Label(text="is equal to")
label.grid(row=1,column=0)
label.config(padx=5,pady=5)

label_km1 = Label(text="0")
label_km1.grid(row=1, column=1)
label_km1.config(padx=5,pady=5)

label_km = Label(text="Km")
label_km.grid(row=1,column=2)
label_km.config(padx=5,pady=5)

def calculate():
    conversion_factor = 0.621
    mile = float(entry_mile.get())
    km = "{:.3f}".format(mile / conversion_factor)
    label_km1.config(text=f"{km}")

button = Button(width=7,text="Calculate",command=calculate,activebackground="skyblue",activeforeground="black"
                ,background="white",borderwidth=2,cursor="heart",relief="raised")
button.grid(row=2,column=1)
button.config(padx=5,pady=5)


window.mainloop()