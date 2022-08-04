from tkinter import *
from tkinter import ttk
import tracker_main

lastCommand = ''


def onEnter(e):
    lastCommand = mainEntry.get()
    try:
        result = tracker_main.cmd(lastCommand)
        if result is None:
            write("처리 성공")
        else:
            write(result)
    except Exception as e:
        write(f"처리 실패 : {e.args[0]}")
    clearMainEntry(None)


def clearMainEntry(dummy):
    mainEntry.delete(0, "end")


def write(message: str):
    outputLable.config(text=message)


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

outputLable = ttk.Label(frm, text="?를 입력하여 도움말 표시")
outputLable.grid(row=2, column=0)

ttk.Button(frm, text="종료", command=root.destroy).grid(row=2, column=1)

root.mainloop()
