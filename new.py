import multiprocessing
from tkinter import *
import tkinter as tk
import cv2
import os

e = multiprocessing.Event()
p = None


def startrecording(e):
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output1.mp4', fourcc, 20, (width, height))

    while (cap.isOpened()):
        if e.is_set():
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            e.clear()
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
        else:
            break


def start_recording_proc():
    global p
    p = multiprocessing.Process(target=startrecording, args=(e,))
    p.start()
    os.system("python gps.py")


def stoprecording():
    e.set()
    p.join()

    os.system('python main.py')

    root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    # root.geometry("%dx%d+0+0" % (400, 600))
    # root.config(bg="sky blue")
    f2 = tk.Frame(width=895, height=534, )
    head1 = PhotoImage(file='B1.png')
    labelphoto = Label(f2, image=head1, )
    labelphoto.pack()

    f2.pack(fill="both", expand=True, padx=20, pady=20)

    log2 = PhotoImage(file='B2.png')

    btn2 = Button(
        f2,
        image=log2,
        command=start_recording_proc,
        borderwidth=0,

        width=0
    )
    btn2.place(x=230, y=290)
    log = PhotoImage(file='B3.png')

    btn2 = Button(
        f2,
        image=log,

        command=stoprecording,
        borderwidth=0,

        width=0
    )
    btn2.place(x=530, y=290)

    root.mainloop()