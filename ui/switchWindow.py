import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import subprocess
import socket
import time


LARGE_FONT= ("Verdana", 12)


class Sharepy(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, SendPage, ReceivePage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        # label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        # label.pack(pady=10,padx=10)
        controller.title("SharePy")
        controller.geometry("400x300")

        self.pack(fill=tk.BOTH, expand=1)

        self.showText()
        self.showImg()

        button = tk.Button(self, text="Send",
                            command=lambda: controller.show_frame(SendPage), width=10)
        button.grid(row=1, column=0, sticky=tk.W)
        button.place(x=50, y=230)
        # button.pack()

        button2 = tk.Button(self, text="Receive",
                            command=lambda: controller.show_frame(ReceivePage), width=10)
        button2.grid(row=1, column=0, sticky=tk.W)
        button2.place(x=250, y=230)
        # button2.pack()


    def showImg(self):
        load = Image.open("idea.png")
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=130, y=50)


    def showText(self):
        text = tk.Label(self, text="Transfer and Receive files")
        text.place(x=130, y=80)
        text.pack()



class SendPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(ReceivePage))
        button2.pack()


class ReceivePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(SendPage))
        button2.pack()

app = Sharepy()
app.mainloop()
