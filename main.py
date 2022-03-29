from tkinter import *
import playground


def button_clicked():
    # my_label.config(text="Button got clicked")
    my_label.config(text=my_input.get())
    print("I got clicked")


window = Tk()
window.title("My First GUI program ")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Creating a label
my_label = Label(text="My First Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Creating buttons
my_button = Button(text="Click me", command=button_clicked)
# my_button.pack()
my_button.grid(column=1, row=1)
second_button = Button(text="Or Me")
second_button.grid(column=2, row=0)


# Creating an Entry (Input)
my_input = Entry(width=10)
# my_input.pack()
my_input.grid(column=3, row=2)


# print(playground.add(1, 2, 3, 4, 5, 6))

window.mainloop()
