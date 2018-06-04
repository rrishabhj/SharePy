import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import subprocess
import socket
import time
import subprocess
import socket               # Import socket module
import time
import os
# from wireless import Wireless
# from access_points import get_scanner


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

        self.ssid=''
        self.passw=0
        self.fadd=''

        tk.Frame.__init__(self, parent)
        # label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        # label.pack(pady=10,padx=10)
        self.pack(fill=tk.BOTH, expand=1)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=0, sticky=tk.W)
        button1.place(x=5, y=5)

        button2 = tk.Button(self, text="Search For Network",
                            command=self.showavailablewifi)
        button2.grid(row=1, column=0, sticky=tk.W)
        button2.place(x=260, y=5)

        #
        text = tk.Label(self, text="SSID")
        text.place(x=50, y=35)

        text2 = tk.Label(self, text="Password")
        text2.place(x=50, y=55)
        # #
        e1 = tk.Entry(self)
        e1.place(x=110, y=35)

        e2 = tk.Entry(self)
        e2.place(x=110, y=55)

        button3 = tk.Button(self, text='Connect', command=lambda: self.connect_to_network)
        button3.place(x=50, y=90)

        label = tk.Label(self, text="Connect to the server network", font=LARGE_FONT)
        label.place(x=80, y=150)

        button4 = tk.Button(self, text="Select File", command=self.load_file, width=10)
        button4.grid(row=1, column=0, sticky=tk.W)
        button4.place(x=130, y=230)

        button5 = tk.Button(self, text="Send", command=lambda: self.send_file, width=10)
        button5.grid(row=1, column=0, sticky=tk.W)
        button5.place(x=130, y=260)


    def showavailablewifi(self):
        python3_command = "/home/rishabh/cowrks/searchingwifi.py" # launch your python2 script using bash

        process = subprocess.Popen(python3_command , stdout=subprocess.PIPE)
        output, error = process.communicate()  # receive output from the python2 script
        print(output)
        # inflate the res from output to screen

    def connect_to_network(self):

        self.ssid = e1.get()
        self.passw = e2.get()
        python3_command = "/home/rishabh/cowrks/connectwifi.py" + self.ssid + self.passw   # launch your python2 script using bash

        process = subprocess.Popen(python3_command , stdout=subprocess.PIPE)
        output, error = process.communicate()
        # output gives the status if its conn ot not
        # print(output)

    def load_file(self):

        # Types and formats of files
        self.fadd = askopenfilename(filetypes=(("Image", "*.png"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))
        if fname:
            try:
                print("File Selected")
                print(self.fadd)
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return

    def send_file(self):

        s = socket.socket()         # Create a socket object
        host =  '192.168.0.101'
        port = 12345                 # Reserve a port for your service.

        s.connect((host, port))
        # s.send("Hello server!")
        faddress = self.fadd
        fname = os.path.basename(faddress)
        s.send(fname)
        time.sleep(0.2)

        f = open(faddress,'rb')
        print('Sending...')
        l = f.read(1024)
        while (l):
            print('Sending...')
            s.send(l)
            l = f.read(1024)
            time.sleep(0.2)

        f.close()
        print("Done Sending")
        print(s.recv(1024))
        s.close()                  # Close the socket when done



class ReceivePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.pack(fill=tk.BOTH, expand=1)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=0, sticky=tk.W)
        button1.place(x=5, y=5)

        button2 = tk.Button(self, text="Create HotSpot",
                            command=self.create_hotspot)
        button2.grid(row=1, column=0, sticky=tk.W)
        button2.place(x=260, y=5)


        label = tk.Label(self, text="Status: Not Connected", font=LARGE_FONT)
        label.place(x=85, y=100)

        button3 = tk.Button(self, text='Start Server', command=lambda: self.start_server)
        button3.place(x=130, y=180)

    def create_hotspot(self):
        print("Creating Hotspot")
        subprocess.call(r"/home/rishabh/cowrks/task1/WIFI-module/hotspotOn.sh")
        print("Hotspot Created")

    def start_server():

        # make the socket
        s = socket.socket()         # Create a socket object
        host = '0.0.0.0' # Get local machine name
        port = 12345                 # Reserve a port for your service.
        s.bind((host, port))        # Bind to the port

        s.listen(5)                 # Now wait for client connection.
        while True:
            c, addr = s.accept()     # Establish connection with client.
            print('Got connection from', addr)
            print("Receiving...")
            fname = c.recv(1024)
            print(fname)
            f = open(fname,'wb')

            # start receiving file
            l = c.recv(1024)
            while (l):
                print("Receiving...")
                f.write(l)
                l = c.recv(1024)
                if len(l) < 1024:
                    break
                time.sleep(0.2)

            f.close()
            print("Done Receiving")
            s.shutdown(socket.SHUT_WR)
            out = 'Thank you for connecting'
            c.sendall(out.encode('utf-8'))
            c.close()
        s.close()


app = Sharepy()
app.mainloop()
