from tkinter import *
from tkinter import ttk
import tracker_main

lastCommand = ''


def onEnter(e):
    lastCommand = mainEntry.get()
    tracker_main.cmd(lastCommand)


def clearMainEntry(first):
    mainEntry.delete(0, "end")


root = Tk()
root.title("메이플 옥션 트래커")
frm = ttk.Frame(root, padding=10)
frm.grid()

mainEntry = ttk.Entry(frm)
mainEntry.grid(row=0, column=0)
mainEntry.focus()


ttk.Button(frm, text="Enter", command=None).grid(row=0, column=1)
root.bind("<Return>", onEnter)
root.bind("<Control-c>", exit)
root.bind("<Control-d>", exit)
root.bind("<Control-l>", clearMainEntry)


ttk.Button(frm, text="종료", command=root.destroy).grid(row=2, column=1)

root.mainloop()
