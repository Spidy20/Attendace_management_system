import tkinter as tk
from tkinter import Message, Text
import os
import shutil
import csv
import numpy as np
from PIL import Image,ImageTk
import cv2 
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font

window = tk.Tk()
window.title("Face_Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
window.geometry('1280x720')
window.configure(background='snow')

def clear():
    txt.delete(first=0, last=22)

def clear1():
    txt2.delete(first=0, last=22)

def take_img():
    try:
        cam = cv2.VideoCapture(0)
        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        stat = 'We are getting your face images.....'
        Notification.configure(text=stat, bg="SpringGreen2", width=23)
        Notification.place(x=350, y=400)
        Enrollment = txt.get()
        Name = txt2.get()
        path = 'C:/Users/kusha/PycharmProjects/Attendace managemnt system/Datasets/' + Enrollment + ' ' + Name
        new_path = 'C:/Users/kusha/PycharmProjects/Attendace managemnt system/Datasets/' + Enrollment + ' ' + Name + '/'
        os.mkdir(path)
        sampleNum = 0

        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder
                cv2.imwrite(new_path + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                cv2.imshow('frame', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 150:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for Enrollment : " + Enrollment + " Name : " + Name
        Notification.configure(text=res, bg="SpringGreen3", width=50,font=('times',18, 'bold'))
        Notification.place(x=350, y=400)

    except FileExistsError as F:
        f='Student Data already exists'
        Notification.configure(text=f, bg="Red",width=21)
        Notification.place(x=450, y=400)



window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="Face-Recognition-Based-Attendance-Management-System", bg="SpringGreen3", fg="white", width=50,
                   height=3, font=('times', 30, 'italic bold '))

message.place(x=80, y=20)

Notification = tk.Label(window, text="All things good", bg="Green", fg="white", width=15,
                   height=3, font=('times', 17, 'bold'))

lbl = tk.Label(window, text="Enter Enrollment", width=20, height=2, fg="red", bg="yellow", font=('times', 15, ' bold '))
lbl.place(x=200, y=200)

txt = tk.Entry(window, width=20, bg="yellow", fg="red", font=('times', 25, ' bold '))
txt.place(x=550, y=210)

lbl2 = tk.Label(window, text="Enter Name", width=20, fg="red", bg="yellow", height=2, font=('times', 15, ' bold '))
lbl2.place(x=200, y=300)

txt2 = tk.Entry(window, width=20, bg="yellow", fg="red", font=('times', 25, ' bold '))
txt2.place(x=550, y=310)


clearButton = tk.Button(window, text="Clear",command=clear,fg="white"  ,bg="deep pink"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=210)

clearButton1 = tk.Button(window, text="Clear",command=clear1,fg="white"  ,bg="deep pink"  ,width=10 ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton1.place(x=950, y=310)

takeImg = tk.Button(window, text="Take Images",command=take_img,fg="white"  ,bg="blue2"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
takeImg.place(x=200, y=500)

trainImg = tk.Button(window, text="Train Images"  ,fg="white"  ,bg="purple2"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
trainImg.place(x=500, y=500)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="white"  ,bg="Red"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=800, y=500)

window.mainloop()