from tkinter import *

window = Tk()

window.title("Flashcards")

label1 = Label(window, text="Enter: ")
label1.grid(row=1, column=0, sticky=E)

label2 = Label(window, text="The CPU is responsible for...")

entry1 = Entry(window, width=20, bg="light blue")
entry1.grid(row=2, column=0, sticky=E)

def button_click():
    typed_text = entry1.get()

    print(typed_text)

button1 = Button(window,text="Motherboards", width=10, command=button_click)
button1.grid(row=1, column=2, sticky=E)

button2 = Button(window,text="Memory", width=10, command=button_click)
button2.grid(row=2, column=2, sticky=E)

button3 = Button(window,text="Storage Devices", width=10, command=button_click)
button3.grid(row=3, column=2, sticky=E)

output_text = Text(window, width=40, height=10, wrap=WORD, background = "blue")
output_text.grid(row=4, column=0, columnspan=2, sticky = E)

my_dictionary = ["Motherboards", "Storage Devices", "Memory]


window.mainloop()
