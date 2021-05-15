import pyqrcode
import png
from pyqrcode import QRCode
from datetime import datetime
from datetime import time
import time
from tkinter import *
import threading

latest = datetime.now()
date_time = latest.strftime("%m-%d-%Y-%H-%M")
print(date_time)
current_time = datetime.now()
def ctime():
    current_time = datetime.now()
    global ct
    ct = current_time.strftime("%M")
    ct = int(ct) + 1
    if ct<10:
        ct = str(ct)
        ct = '0' + ct
    else:
        ct = str(ct)     
ctime()



def QR():
    #quit = " "
    #while quit != "q":
    latest = datetime.now()
    date_time = latest.strftime("%m-%d-%Y-%H-%M")   
    # String which represents the QR code
    s = date_time

    # Generate QR code
    url = pyqrcode.create(s)

    # Create and save the png file naming "myqr.png"
    url.png('myqr.png', scale = 6)
    #from try2 import showqr
    showqr()
    print( "QR Changed")

def showqr():
    root = Tk()      
    canvas = Canvas(root, width = 300, height = 300)      
    canvas.pack()
    img = PhotoImage(file="myqr.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    mainloop()
    
def repeat():
    z = datetime.now()
    zl = z.strftime("%M")
    time.sleep(1)
    if zl == ct:
        ctime()
        QR()    
        print("Process Complete")

while True: 
    repeat()
     

    
        
