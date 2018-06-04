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
        button = Button(self, text="select", command=self.load_file, width=10)
        button.grid(row=1, column=0, sticky=W)
        button.place(x=150, y=230)

        self.showText()
        self.showImg()

    def load_file(self):

        # Types and formats of files
        fname = askopenfilename(filetypes=(("Image", "*.png"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))
        if fname:
            try:
                print("Init sending file to Server")
                print(fname)

                # print("Creating Hotspot")
                # subprocess.call("hotspotOn.sh")
                # print("Hotspot Created")

                s = socket.socket()

                # connected_device_ip
                host = '192.168.0.103'

                # Reserve a port for service.
                port = 12345

                s.connect((host, port))

                # s.send("Hello server!")
                f = open('tosend.png','rb')
                print('Sending...')
                l = f.read(1024)
                while (l):
                    print('Sending...')
                    s.send(l)
                    l = f.read(1024)
                f.close()
                print("Done Sending")
                print(s.recv(1024))
                # Close the socket
                s.close

            except Exception, arg:
                print(arg)
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return

    def showImg(self):
        load = Image.open("idea.png")
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=130, y=50)


    def showText(self):
        text = Label(self, text="Select the file for transfer")
        text.pack()


    def client_exit(self):
        exit()

root = Tk()

root.geometry("400x300")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
