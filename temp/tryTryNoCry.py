from tkinter import *

def submit():
    username = entry.get()
    print("hello"+username)

def delete():
    entry.delete(0,END)#deletes the line of text

window = Tk()

# creating a button
submit = Button(window, text="goom", command=submit)
submit.pack(side=RIGHT)


entry = Entry()
entry.config(font=('Ubuntu',50))
entry.config(bg='#111111')
entry.config(fg='Green')

# entry.insert(0,'rishabh enter here')

# entry.config(state=DISABLED)#active or disabled

entry.config(width=10)
# entry.config(=10)

# entry.config(show='*')#submitting a password or something

entry.pack()
window.mainloop()
