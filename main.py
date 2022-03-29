from tkinter import *
import playground

window = Tk()
window.title("My First GUI program ")
window.minsize(width=500, height=300)

# Creating a label
my_label = Label(text="My First Label", font=("Arial", 24, "bold"))
my_label.pack()


# Creating a button
def button_clicked():
    # my_label.config(text="Button got clicked")
    my_label.config(text=my_input.get())
    print("I got clicked")


my_button = Button(text="Click me", command=button_clicked)
my_button.pack()

# Creating an Entry (Input)
my_input = Entry(width=10)
my_input.pack()
# new_label = my_input.get()



print(playground.add(1, 2, 3, 4, 5, 6))

window.mainloop()
