import cv2
from tkinter import *
from PIL import Image, ImageTk
import sys

def onClossing():
    root.quit()
    cap.relase()
    print("Camara desconocida")
    root.destroy()

def callback():
    ret, frame = cap.read()

    if ret:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = thumbnail((400,400))
        img = ImageTk.PhotoImage(image=img)
        label.configure(image = tkimage)
        label.image = tkimage
        label.after(1, callback)
    else:
        onClossing()

url = "http://192.168.1.111"
cap = cv2.VideoCapture(url)

if cap.isOpened():
    print("Camara inicializada")

else:
    sys.exit("Camara desconectada")

root = Tk()
root.protocol("WM_DELETE_WINDOW", onClossing)
root.title("Video Stream")
root.geometry("400x400")

Label = Label(root)