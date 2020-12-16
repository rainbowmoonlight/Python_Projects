from tkinter import *

window = Tk()
window.title("Mi/Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

input = Entry(width=15)
input.insert(END, string="0")
input.grid(column=1, row=0)

label_source = Label(text="miles", font=("Arial", 12, "normal"))
label_source.grid(column=2, row=0)
label_source.config(padx=20)

label_equal = Label(text="is equal to", font=("Arial", 12, "normal"))
label_equal.grid(column=0, row=1)

factor = 1.609344
label_value = Label(text="0", font=("Arial", 12, "bold"))
label_value.grid(column=1, row=1)


def calc_result():
    miles = float(input.get())
    kms = round(miles * factor, 2)
    label_value.config(text=str(kms))


label_target = Label(text="km", font=("Arial", 12, "normal"))
label_target.grid(column=2, row=1)

button = Button(text="Calculate", command=calc_result)
button.grid(column=1, row=2)


def default2miles():
    global factor
    label_source.config(text="miles")
    label_target.config(text="km")
    factor = 1.609344
    calc_result()


def default2km():
    global factor
    label_source.config(text="km")
    label_target.config(text="miles")
    factor = 0.62137
    calc_result()


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Mi->Km", value=0, variable=radio_state, command=default2miles)
radiobutton2 = Radiobutton(text="Km->Mi", value=1, variable=radio_state, command=default2km)
radiobutton1.grid(column=1, row=4)
radiobutton2.grid(column=1, row=5)

window.mainloop()
