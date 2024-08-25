from tkinter import Tk, Label, Button, Entry

window = Tk()

lable = Label(text="Hello :)")
lable.pack()


_input =  Entry()
_input.pack()

def get_input_text():
    print(_input.get())


button = Button(
    text="click my",
    width=25,
    height=5,
    bg="red",
    fg="blue",
    command = get_input_text
    
)
button.pack()






window.mainloop()