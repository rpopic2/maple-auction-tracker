from sys import *
from tkinter import *
from tkinter import ttk

import pandas as pd
from pandas import DataFrame
import tracker_main
import datagen
import matplotlib.pyplot as plt

lastCommand = ''


def dummyOnEnter(e):
    onEnter()


def onEnter():
    global lastCommand
    lastCommand = mainEntry.get()
    try:
        result = tracker_main.cmd(lastCommand)
        if result is None:
            write("처리 성공")
            if lastCommand.startswith("불러오기"):
                print_welcome_screen()
        else:
            write(result)
            if lastCommand.startswith("그래프"):
                plt.show()
    except Exception as err:
        write(f"처리 실패 : {err.args[0]}")
    clearMainEntry(None)


def clearMainEntry(dummy):
    mainEntry.delete(0, "end")


def loadLastCmd(dummy):
    global lastCommand
    clearMainEntry(None)
    mainEntry.insert(0, lastCommand)


def write(message: str):
    outputLable.config(text=message)

def print_welcome_screen():
    statusbarLable.config(text=datagen.dataSet)
    df = tracker_main.getData()
    uniques = df.drop_duplicates(subset='itemname', keep='last')
    outputLable.config(text=f"{getHelpText}\n{uniques}")

getHelpText = "?를 입력하여 도움말 표시"

root = Tk()
root.title(f"메이플 옥션 트래커 v.{tracker_main.__version__}")
frm = ttk.Frame(root, padding=10)
frm.grid()

mainEntry = ttk.Entry(frm)
mainEntry.grid(row=0, column=0)
mainEntry.focus()

ttk.Button(frm, text="Enter", command=onEnter).grid(row=0, column=1)
root.bind("<Return>", dummyOnEnter)
root.bind("<Control-d>", exit)
root.bind("<Control-l>", clearMainEntry)
root.bind("<Up>", loadLastCmd)

statusbarLable = ttk.Label(frm)
statusbarLable.grid(row=2, column=0)
outputLable = ttk.Label(frm)
print_welcome_screen()

outputLable.grid(row=3, column=0)


root.mainloop()
