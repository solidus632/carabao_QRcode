# Import Module
from tkinter import *
from PIL import Image, ImageTk
import cv2
import easygui

id_user = 0
# create root window
root = Tk()

# root window title and dimension
root.title("Carabao folklift")
# Set geometry(widthxheight)
root.geometry('1280x720')

# adding a label to the root window
lbl = Label(root, text="Are you a Geek?")
lbl.grid(column=0, row=1)

# # adding Entry Field
# txt = Entry(root, width=10)
# txt.grid(column=0, row=2)

dir_img_user = ImageTk.PhotoImage(Image.open(r"C:\Users\pe_wi\Downloads\user.png"))
img_user = Label(image=dir_img_user)
img_user.grid(column=0, row=0)


# function to display user text when
# button is clicked
def clicked():
    global id_user
    id_user = easygui.enterbox(msg="Insert your ID Card")
    print(id_user, type(id_user))

    res = id_user
    lbl.configure(text=res)


# button widget with red color text inside
btn = Button(root, text="Click me", command=clicked)
# Set Button Grid
btn.grid(column=0, row=3)

location_now = Label(root, text="Location",font=("Arial", 90))
location_now.grid(column=3, row=3)

# Create a Label to capture the Video frames
label = Label(root)
label.grid(row=0, column=3)
cap = cv2.VideoCapture(0)
# Define function to show frame
detector = cv2.QRCodeDetector()

def show_frames():
    # Get the latest frame and convert into Image
    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label.after(20, show_frames)
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(cv2image)
    if data:
        # check if there is a QRCode in the image
        print(data)
        location_now.configure(text=data)


show_frames()

# Execute Tkinter
root.mainloop()
