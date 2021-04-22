from tkinter import *

window = Tk()

my_dictionary = {"CPU": "Central processing unit is the brains of the computer, helps process everything", "RAM": "Random Access Memory - helps multiple things run at once", }

window.title("Flashcards")

label1 = Label(window, text="Enter: ")
label1.grid(row=1, column=0, sticky=E)

label2 = Label(window, text="")

entry1 = Entry(window, width=20, bg="light blue")
entry1.grid(row=2, column=0, sticky=E)

def delet():
    output_text.delete(0,0, END)


def cpu_button_click():
    output_text.delete(0.0, END)
    Screentxt = (my_dictionary["CPU"])
    output_text.insert(END, Screentxt)
   
    

def ram_button_click():
    output_text.delete(0.0, END)
    Screentxt = (my_dictionary["RAM"])
    output_text.insert(END, Screentxt)
    
cpu_button1 = Button(window,text="CPU", width=10, command=cpu_button_click)
cpu_button1.grid(row=1, column=2, sticky=E)

button2 = Button(window,text="RAM", width=10, command=ram_button_click)
button2.grid(row=2, column=2, sticky=E)



output_text = Text(window, width=40, height=10, wrap=WORD, background = "blue")
output_text.grid(row=4, column=0, columnspan=2, sticky = E)




window.mainloop()
