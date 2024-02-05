from tkinter import *


def calculate_bmi():
    weight = float(weight_input.get())
    height = float(height_input.get())
    bmi = round(weight/(height*height))
    bmi_input.config(text=f"{bmi}")


window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

weight_label = Label(text="Weight (kg)")
weight_label.grid(column=1, row=1)

# Entry for weight
weight_input = Entry()
weight_input.grid(column=2, row=1)

height_label = Label(text="Height (m)")
height_label.grid(column=1, row=3)

# Entry for Height
height_input = Entry()
height_input.grid(column=2, row=3)

bmi_label = Label(text="BMI")
bmi_label.grid(column=1, row=5)

bmi_input = Label(text="0")
bmi_input.grid(column=2, row=5)


# Calculate Button
calculate_button = Button(text="Calculate", command=calculate_bmi)
calculate_button.grid(column=2, row=7)

window.mainloop()
