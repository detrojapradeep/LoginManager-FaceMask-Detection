import cv2
from cv2 import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from datetime import datetime
from datetime import time
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import * 
from functools import partial
import mysql.connector
from PIL import Image, ImageTk

#import test.py

#DB connections
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root1590',
    database = 'employee'
)
myquery = mydb.cursor()

#scanner
print(eid)
cap = cv2.VideoCapture(0)
i=0
latest = datetime.now()
date_time = latest.strftime("%m-%d-%Y-%H-%M")
print(date_time)

while i<1:
    _, frame = cap.read()
    decodedobjects = pyzbar.decode(frame)
    #print(decodedobjects)
    for obj in decodedobjects:
        print(obj.data.decode("utf-8"))
        
        if obj.data.decode("utf-8") == date_time:
            print("Present")
            q = 'Insert into employee_attend values(' + eid + ',now());'
            myquery.execute(q)
            mydb.commit()
        
        else:
            print("Absent")
            scan()
        
        i=i+1
    
    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)
    
cv2.destroyAllWindows()
tkWindow.destroy()

        

#login_window
tkWindow = tk.Tk()
tkWindow.geometry('400x150')
tkWindow.title("Login")

#id
idLabel = Label(tkWindow, text = "ID").grid(row=0, column=0)
id = StringVar()
idGet = Entry(tkWindow, textvariable = id).grid(row=0, column=1)

#password
passwordLabel = Label(tkWindow, text = "Password").grid(row=1, column=0)
password = StringVar()
passwordGet = Entry(tkWindow, textvariable = password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin,id,password)

#login_button
loginButton = Button(tkWindow, text="Login", command = validateLogin).grid(row=4,column=0)


tkWindow.mainloop()
