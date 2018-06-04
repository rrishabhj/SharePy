from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import subprocess
import socket
import time

class Window(Frame):

    # Define settings
    def __init__(self, master=None):

        Frame.__init__(self, master)

        # Master widget reference
        self.master = master

        # init para of window
        self.init_window()

    # Creation of Window Para
    def init_window(self):

        self.master.title("SharePy")

        # allowing the widget to take the full space
        # of the root window
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)

        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # self.caCanvas(top, bg="blue", height=250, width=300)
        button = Button(self, text="Send", width=10)
        button.grid(row=1, column=0, sticky=W)
        button.place(x=250, y=230)

        # self.caCanvas(top, bg="blue", height=250, width=300)
        button = Button(self, text="Receive", command=self.load_file, width=10)
        button.grid(row=1, column=0, sticky=W)
        button.place(x=50, y=230)

        self.showText()
        self.showImg()

    def showImg(self):
        load = Image.open("idea.png")
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=130, y=50)


    def showText(self):
        text = Label(self, text="Transfer and Receive files")
        text.pack()


    def client_exit(self):
        exit()

root = Tk()

root.geometry("400x300")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
