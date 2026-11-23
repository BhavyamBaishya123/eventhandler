from tkinter import*
window=Tk()
window.title("event handler")
window.geometry("250x200")
def keypress(event):
    print(event.char)
window.bind("<Key>",keypress)
def button_clicker(event):
    print("The button was click")
b=Button(text="click")
b.pack()
b.bind("<Button-1>",button_clicker)
window.mainloop()