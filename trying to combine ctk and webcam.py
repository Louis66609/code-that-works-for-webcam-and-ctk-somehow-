import customtkinter as ctk
import tkinter
import customtkinter
from PIL import ImageTk, Image
import re
import cv2

cascadeFace = cv2.CascadeClassifier("frontalface.xml")

window = ctk.CTk()
window.geometry("1400x800")

frame = ctk.CTkFrame(master=window, width=850, height=600)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

label = ctk.CTkLabel(master=window, text="")
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

tabview = customtkinter.CTkTabview(frame, width=850, height=615, corner_radius=15)
tabview.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

overview_tab = tabview.add("Live Feed")
attendance_tab = tabview.add("Attendance")

cap = cv2.VideoCapture(0)
show_webcam = True

def update():
    global show_webcam
    if show_webcam and tabview._current_name == "Live Feed":
        ret, image = cap.read()

        if ret:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = cascadeFace.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 225, 0), 2)

            photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
            label.configure(image=photo)
            label.image = photo 

    tabview.after(10, update)
    if show_webcam and tabview._current_name == "Live Feed":


update()
window.mainloop()
cap.release()
cv2.destroyAllWindows()

